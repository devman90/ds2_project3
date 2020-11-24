# Samsung DS2 - Gas concentration prediction
## Predicting gas concentration using sensor data

Link: https://www.kaggle.com/c/samsung-ds2-ds6-traffic-occupancy-rate/

### Description
이 in-class Kaggle competition에서는 가스 센서데이터를 활용하여 CO농도를 예측하는 모델을 구현합니다. CO 가스 농도는 14개의 금속산화물 센서로 측정되었으며, 25h 동안의 CO 농도변화를 한번의 실험셋트로 정의하고, 총 13일동안 13번의 실험셋트를 수행하여 수집된 데이터 입니다. 12일 동안 측정된 데이터(train1~train12.csv)를 이용해 마지막 날 데이터(test_x.csv)의 CO농도를 예측하는 모델을 구현하는 것이 과제목표 입니다. 데이터셋에 대한 상세 내용은 아래 링크를 참고하세요. https://archive.ics.uci.edu/ml/datasets/Gas+sensor+array+temperature+modulation 모델을 통해 얻은 예측 결과는 하루 20회까지 submission할 수 있으며, MAE(Mean Absolute Error)로 평가됩니다.  

### Code submission
본 competition은 public dataset을 가공하여 진행하는 문제이다보니 부정행위의 우려가 있어 코드를 함께 제출받습니다. Reproducing이 가능하도록 모든 random seed 를 고정하여 사용해주시길 부탁드립니다. 11월 30일 오후에 발표가 끝난 후 조교가 돌릴 수 있는 버전의 코드를 자정까지 (2020.11.31 00:00) 조교 이메일(ej-lee@snu.ac.kr)로 제출해주시길 바랍니다.  

### Evaluation
모델 평가 matrix은 MAE(Mean Absolute Error)입니다.  
https://en.wikipedia.org/wiki/Mean_absolute_error
