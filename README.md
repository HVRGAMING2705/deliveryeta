# DeliveryETA — Food Delivery Time Predictor

A 2nd-year B.Tech AI/ML project by Vikranth Reddy (Woxsen University).

Ridge regression (alpha=1.0) on standardized features — distance (km), restaurant prep time (min), traffic level (1-5), number of items, rider experience (years), peak hour — trained on 600 synthetic food delivery orders (seed 42).

- 5-fold CV R&sup2;: 0.919, MAE: 2.41 min (mean-guess baseline MAE: 8.46 min); mean delivery time 47.9 min
- Live demo: https://deliveryeta-delta.vercel.app (runs fully in the browser — no backend)
- `train.py` trains the model and writes `model.json`; `index.html` applies the same weights in JavaScript.

Note: classroom demo on synthetic orders — real delivery times also depend on the exact route, weather, the restaurant's live queue and the rider's actual path.
