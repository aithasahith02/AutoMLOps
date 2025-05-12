import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'api')))

from predict_pipeline import predict

test_input = {
    "mean radius": 14.2,
    "mean texture": 20.0,
    "mean perimeter": 90.0,
    "mean area": 600.0,
    "mean smoothness": 0.1,
}

print(predict(test_input))

