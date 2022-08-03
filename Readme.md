# Continuous performance evaluation for business process outcome monitoring

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

<img src="https://render.githubusercontent.com/render/math?math=F = \frac{\sum_{D_i \in \mathbb{D}(\theta)} \rvert D_i\lvert}{\rvert \theta \lvert}">

<img src="https://render.githubusercontent.com/render/math?math={\color{white}F = \frac{\sum_{D_i \in \mathbb{D}(\theta)} \rvert D_i\lvert}{\rvert \theta \lvert}#gh-dark-mode-only">

#### b) Continuous evaluation by case duration
_"How likely is the framework to output a correct prediction when x% of its duration has elapsed?"_

This type of evaluation is similar to the previous one, however, in this case the progress of a case is identified by the time elapsed since the beginning of it.

### 2) Real-time model performance
_“How likely are the most recentprediction(s) obtained from a model to be eventually correct?”_

 In the real-time method we first define w as the size of a test window containing the traces associated with the latest W labels <img src="https://render.githubusercontent.com/render/math?math=y_w"> that have been received. Then consider the  average of the performance across all the predictions available, at any prefix length, for each trace in this window.

