docker run --gpus=1 --rm --net=host -v ${PWD}/models:/models ner tritonserver --model-repository=/models
