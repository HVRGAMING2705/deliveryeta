from pptx import Presentation
from pptx.util import Inches, Pt
import sys
DOMAIN = sys.argv[1] if len(sys.argv) > 1 else "deliveryeta.vercel.app"
prs = Presentation(); prs.slide_width = Inches(13.33); prs.slide_height = Inches(7.5)
def add(i, title, lines):
    s = prs.slides.add_slide(prs.slide_layouts[1])
    s.shapes.title.text = title
    tf = s.placeholders[1].text_frame; tf.word_wrap = True
    for j, ln in enumerate(lines):
        p = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
        p.text = ln; p.font.size = Pt(20); p.space_after = Pt(10)
add(0, "DeliveryETA — Food Delivery Time Predictor", ["An AI/ML project by Vikranth Reddy", "B.Tech CSE (AI & ML), 2nd Year — Woxsen University", "A model that looks at your order — distance, prep time, traffic, order size, rider experience — and predicts when your food will arrive"])
add(1, "The Problem", ["Food delivery apps show an ETA, but it often feels like a guess: 25 minutes can turn into 50", "Distance, prep time, traffic, order size and peak hours all push the delivery time — but by how much?", "Can a simple, explainable model turn order details into an honest arrival estimate?", "DeliveryETA answers that question with ridge regression anyone can follow"])
add(2, "The Solution — DeliveryETA", ["Enter 6 details: distance, restaurant prep time, traffic level, items, rider experience, peak hour", "The model returns the predicted delivery time instantly", "Try a peak-hour rush order or a quick nearby order with one click", "Runs fully in the browser — no backend, no waiting"])
add(3, "Tech Stack", ["Python + scikit-learn: dataset generation and model training", "Ridge regression (alpha = 1.0) on 6 standardised features", "HTML, CSS and vanilla JavaScript for the interactive demo", "GitHub for source control, Vercel for free hosting"])
add(4, "Architecture", ["Dataset: 600 synthetic food delivery orders built from simple delivery logic", "Order details -> standardisation -> ridge regression -> delivery time in minutes (floored at 10)", "model.json ships with the site; JavaScript applies the same formula", "Training script: train.py; site generator: gen_site.py"])
add(5, "Live Demo", ["Try it: enter the order details and press Predict Delivery Time", "Nearby 3 km order, 15 min prep, clear roads, 2 items, experienced rider, off-peak -> about 23.9 minutes", "Far 12 km order, 40 min prep, jammed traffic, 8 items, new rider, peak hour -> about 73.6 minutes", f"Demo: https://{DOMAIN}"])
add(6, "Results", ["5-fold cross-validation R-squared: 0.919, MAE: 2.41 minutes", "Baseline (always guessing the mean delivery time): MAE 8.46 minutes — about 3.5x worse", "Mean delivery time in the data: 47.9 minutes", "Browser demo matches Python predictions exactly on all test samples"])
add(7, "Future Scope", ["Train on real delivery data from public datasets", "Add features: exact route, weather, restaurant queue and rider GPS", "Show a live ETA that updates as the rider moves", "Compare ETAs across delivery apps for the same order"])
add(8, "Thank You", ["DeliveryETA — Food Delivery Time Predictor", "Vikranth Reddy, B.Tech CSE (AI & ML), Woxsen University", "Source: github.com/HVRGAMING2705/deliveryeta", "Questions welcome!"])
prs.save("/home/hatch/workspace/goals/daily-ai-ml-project-factory/files/AIML_DeliveryETA_2026-11-18.pptx")
print("slides:", len(prs.slides._sldIdLst))
