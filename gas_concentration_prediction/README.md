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

### Data Description
A chemical detection platform composed of 14 temperature-modulated metal oxide semiconductor (MOX) gas sensors was exposed to dynamic mixtures of carbon monoxide (CO) and humid synthetic air in a gas chamber.  
  
The acquired time series of the sensors and the measured values of CO concentration, humidity and temperature inside the gas chamber are provided.  
  
a) Chemical detection platform: The chemical detection platform was composed of 14 MOX gas sensors that generate a time-dependent multivariate response to the different gas stimuli. The utilized sensors were made commercially available by Figaro Engineering (7 units of TGS 3870-A04) and FIS (7 units of SB-500-12). The operating temperature of the sensors was controlled by the built-in heater, which voltage was modulated in the range 0.2-0.9 V in cycles of 20 and 25 s, following the manufacturer recommendations. The sensors were pre-heated for one week before starting the experiments.  
  
b) Generator of dynamic gas mixtures Dynamic mixtures of CO and humid synthetic air were delivered from high purity gases in cylinders to a small-sized polytetrafluoroethylene (PTFE) test chamber (250 cm3 internal volume), by means of a piping system and mass flow controllers (MFCs). Gas mixing was performed using mass flow controllers (MFC),which controlled three different gas streams (CO, wet air and dry air). These streams were delivered from high quality pressurized gases in cylinders. The selected MFCs (EL-FLOW Select, Bronkhorst) had full scale flow rates of 1000 mln/min for the dry and wet air streams and 3 mln/min for the CO channel. The CO bottle contained 1600 ppm of CO diluted in synthetic air with 21 ± 1% O2. The relative uncertainty in the generated CO concentration was below 5.5%. The wet and dry air streams were both delivered from a synthetic air bottle with 99.995% purity and 21 ± 1% O2. Humidification of the wet stream was based on the saturation method using a glass bubbler (Drechsler bottles).  

c) Temperature/humidity values A temperature/humidity sensor (SHT75, from Sensirion) provided reference humidity and temperature values inside the test chamber with tolerance below 1.8% r.h. and 0.5 ºC, respectively, every 5 s. The temperature variations inside the gas chamber, for each experiment, were below 3 ºC.  

d) Experimental protocol: Each experiment consisted on 100 measurements: 10 experimental concentrations uniformly distributed in the range 0-20 ppm and 10 replicates per concentration. Each replicate had a relative humidity randomly chosen from a uniform distribution between 15% and 75% r.h. At the beginning of each experiment, the gas chamber was cleaned for 15 min using a stream of synthetic air at a flow rate of 240 mln/min. After that, the gas mixtures were released in random order at a constant flow rate of 240 mln/min for 15 min each. A single experiment lasted 25 hours (100 samples x 15 minutes/sample) and was replicated on 13 working days spanning a natural period of 17 days.  

Attribute Information: The dataset is presented in 13 text files, where each file corresponds to a different measurement day. Each file includes the acquired time series, presented in 20 columns: Time (s), CO concentration (ppm), Humidity (%r.h.), Temperature (ºC), Flow rate (mL/min), Heater voltage (V), and the resistance of the 14 gas sensors: R1 (MOhm), R2 (MOhm), R3 (MOhm), R4 (MOhm), R5 (MOhm), R6 (MOhm), R7 (MOhm), R8 (MOhm), R9 (MOhm), R10 (MOhm), R11 (MOhm), R12 (MOhm), R13 (MOhm), R14 (MOhm) Resistance values R1-R7 correspond to FIGARO TGS 3870 A-04 sensors, whereas R8-R14 correspond to FIS SB-500-12 units. The time series are sampled at 3.5 Hz.  

#### File descriptions  
train1~train12.csv - the training set  
test_x.csv - the test set  
sample_submission.csv - a sample submission file in the correct format  
