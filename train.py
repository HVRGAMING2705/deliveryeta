import json
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_predict, KFold
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

rng = np.random.default_rng(42)
N = 600  # synthetic food delivery orders

distance = rng.uniform(1.0, 15.0, N)        # restaurant-to-customer distance in km
prep = rng.uniform(5.0, 45.0, N)            # restaurant prep time in minutes
traffic = rng.integers(1, 6, N).astype(float)  # traffic level 1 (clear) to 5 (jammed)
items = rng.integers(1, 11, N).astype(float)   # number of items in the order
experience = rng.uniform(0.0, 5.0, N)       # rider experience in years
peak = rng.integers(0, 2, N).astype(float)   # 0 off-peak, 1 peak hour

X_raw = np.column_stack([distance, prep, traffic, items, experience, peak])
FEATURES = ["distance", "prep", "traffic", "items", "experience", "peak"]

# Generative delivery time (min): distance and prep are the main drivers;
# heavy traffic and peak hours slow things down; experienced riders are faster.
time = (8
        + 1.2 * distance
        + 0.6 * prep
        + 3.0 * traffic
        + 1.0 * items
        - 0.8 * experience
        + 5.0 * peak
        + rng.normal(0, 3, N))
time = np.clip(time, 10, None)
y = time

mean = X_raw.mean(axis=0)
std = X_raw.std(axis=0)
X = (X_raw - mean) / std

model = Ridge(alpha=1.0).fit(X, y)
kf = KFold(5, shuffle=True, random_state=42)
pred_cv = cross_val_predict(Ridge(alpha=1.0), X, y, cv=kf)
r2 = float(r2_score(y, pred_cv))
mae = float(mean_absolute_error(y, pred_cv))
rmse = float(np.sqrt(mean_squared_error(y, pred_cv)))
base_mae = float(mean_absolute_error(y, np.full(N, y.mean())))
print(f"n={N} mean_time={y.mean():.1f} median_time={np.median(y):.1f}")
print(f"CV R2={r2:.3f} MAE={mae:.2f} RMSE={rmse:.2f} baseline_MAE={base_mae:.2f}")

mj = {"features": FEATURES, "mean": mean.tolist(), "std": std.tolist(),
      "coef": model.coef_.tolist(), "intercept": float(model.intercept_),
      "metrics": {"cv_r2": r2, "cv_mae": mae, "cv_rmse": rmse,
                  "baseline_mae": base_mae, "mean_cost": float(y.mean()), "n": N}}
with open("model.json", "w") as f:
    json.dump(mj, f, indent=1)

def py_pred(row):
    xs = (np.array(row) - mean) / std
    return float(max(model.predict([xs])[0], 10))

samples = [
    [3.0, 15.0, 1, 2, 3.0, 0],   # near, quick prep, clear roads, 2 items, experienced rider, off-peak
    [12.0, 40.0, 5, 8, 0.5, 1],  # far, slow prep, jammed, 8 items, new rider, peak hour
    [7.0, 25.0, 3, 4, 2.0, 0],   # mid distance, mid prep, moderate traffic, 4 items, off-peak
    [2.0, 10.0, 2, 1, 5.0, 0],   # very near, fast prep, light traffic, 1 item, veteran rider
    [14.0, 35.0, 4, 6, 1.0, 1],  # far, slow prep, heavy traffic, 6 items, peak hour
]
for s in samples:
    print(s, "->", round(py_pred(s), 2), "min")
with open("parity_samples.json", "w") as f:
    json.dump([{"row": s, "pred": py_pred(s)} for s in samples], f, indent=1)
