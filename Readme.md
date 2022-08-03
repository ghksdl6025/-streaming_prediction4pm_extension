# Continuous performance evaluation for business process outcome monitoring

## Suhwan Lee<sup>a</sup>, Marco Comuzzi<sup>b</sup>, and Xixi Lu<sup>a</sup>

<sup>a</sup>Utrecht University
<sup>b</sup>Ulsan National Institute of Science and Technology

## General framework
<p align="center">
    <img src="./img/general_framework_a-1.png">
    <br>
    <em>1.a)&nbsp Processing of an event without label</em>
    <img src="./img/general_framework_b-1.png">
    <br>
    <em>1.b)&nbsp Processing of an event with label</em>
</p>

### In this figure, the processing of one event belonging to trace is schematised.
---

First of all, the labels received are only used to train the models in the framework. The event <img src="https://render.githubusercontent.com/render/math?math=e_{k,j}"> may either be the last of <img src="https://render.githubusercontent.com/render/math?math=\sigma_j">, i.e., length of <img src="https://render.githubusercontent.com/render/math?math=j">, in which case the label <img src="https://render.githubusercontent.com/render/math?math=y_j"> becomes known, or not. When an event is not the last one of its trace (see Fig. 1.a), it is used to generate a new prefix of <img src="https://render.githubusercontent.com/render/math?math=\sigma_j"> for prefix <img src="https://render.githubusercontent.com/render/math?math=k">. Then, a prediction <img src="https://render.githubusercontent.com/render/math?math=\hat{y}_{k,j}"> for the new prefix can be computed using the model for prefix <img src="https://render.githubusercontent.com/render/math?math=k">. Receiving the last event <img src="https://render.githubusercontent.com/render/math?math=e_{k,j}">, and its label (see Fig. 1.b) enables (i) to evaluate all the predictions <img src="https://render.githubusercontent.com/render/math?math=\hat{y}_j"> that have been generated for all prefixes <img src="https://render.githubusercontent.com/render/math?math=\sigma_j"> (evaluation before training), (ii) to update the models <img src="https://render.githubusercontent.com/render/math?math=pom_n"> owing to the availability of new labelled prefixes. Finally, it is possible (iii) to compute a new set of predicted labels <img src="https://render.githubusercontent.com/render/math?math=\hat{y}_{k,l}">, with <img src="https://render.githubusercontent.com/render/math?math=l\neq j"> and for all the prefixes for which a label has not been yet received (train and retest).  



## Performance evaluation
### Moving windows and predictive framework

<p align="center">
    <img src="./img/exampleApproachUnfolded-1.png">
    <br>
    <em>2) Updating the moving window of predictions across model updates</em>
</p>

### The four meta-measures
#### 1) Frequency of significant performance drop
_“How often the model performance significantly deviated from (below) the moving average?”_

The evaluation metric captures the rate at which the performance of an online predictive model drops below a certain level considered acceptable.

#### 2) Stability of the performance
_"How volatile are the performance values of the prediction framework?"_

The evaluation metric captures the stability over time of the performance of an online predictive model.

#### 3) Magnitude of performance drop

_“How much is the absolute value of deviated performance of the framework?”_

The evaluation metric captures how much the perfor-
mance of a model normally drops from its expected acceptable level.

#### 4) Recovery rate

_“How quickly can the model be recovered from a sudden change in the prediction ability?”_

The evaluation metric measures the speed at which an online model normally recovers from a performance drop.



