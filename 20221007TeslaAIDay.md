### robot - Optimus

without  tether(线缆)



预期要比车辆的成本更低，低于2w美元

富足的时代，没有贫穷的时代：

- 人们可以拥有他们想要的任何的服务和产品



Tesla 有这样的 entity去做这个事情，促成这样的时代



- 2 order of magnitude improvement in economic ouput 	

![image-20221007123207611](../../Library/Application Support/typora-user-images/image-20221007123207611.png)

人体是很精密的，可以做很多自由度的运动，可以做很复杂的事情

但是生活中的很多事情，并不需要那么多自由度的运动，于是我们简化了人体模型，最终只留下差不多28个自由度。

人体可以做一些很复杂的事，比如从xx拿起小块蛋糕并吃掉，但是，人体并不总是高效的，比如即便我们坐在那里，我们也会消耗能量



我们做的第一件事就是优化Optimus的能耗和效率，这是规模量产的一个重要指标。

我们怎么做呢？

- 我们要尽可能的计算每个部分的能耗



FSD

1. 2000用户到160k用户
2. 一年训练75000个模型，其中281个上线

3. 一个自动驾驶系统应该具备这些功能：
   - 点到点的自动驾驶（？）parsking lot to parking lot
   - 识别红绿灯和停止标志

## Occupancy network

- input：multi-camera video 

- predict：the full physical occupancy of the world around the car（trees/walls/building/cars, whatever physical exists）

  ## lane&objects

  网络会预测有哪些车道线以及他们的connectivity 

  不只是用CV领域的知识，

  输出速度， acc

- 我们扩展了infrastructure，增加了40-50%的算力（？）现在有接近 140000块GPU

- precit vector space

- 路口场景，左转，有个行人横穿，右侧有辆车直行

  - 只管其中一个，很容易忽视另一个，进而被认为是jerk

![image-20221007142714349](../../Library/Application Support/typora-user-images/image-20221007142714349.png)

## planning

- start with vision Measurement ： lane occupancy moving objects
- 基于此，我们再predict set of goal candidate lane s 
- 最后得到 probability mask（和人类认知一致的mask）

![image-20221007143725460](../../Library/Application Support/typora-user-images/image-20221007143725460.png)

左侧的情况同意被惩罚，but how？

![image-20221007143933972](../../Library/Application Support/typora-user-images/image-20221007143933972.png)



use 8-camera data to generate 3D occupancy network

![image-20221007145707824](../../Library/Application Support/typora-user-images/image-20221007145707824.png)

不仅如此，网络还输出 driver‘s surface，不仅有3D geometry还有semantics ，这对山地和曲面情况的自动驾驶有巨大的好处。

所以的路面的预测都是3D的，可以给planning更多的信息



NeRF

occupancy network是用auto-label dataset训练的   ，无需人工参与，应该是用了NeRF相关的技术



## infrastruture

40000 GPU 30PM数据

使用photon图像进行训练

## lane & object

1. 如何预测车道线？

   过去（简单的模型）：image space instance segmentation task

   现在：handle complex manuever

   利用语言模型领域的知识来预测车道线， 

   the word in the tokens are lane 3D position 

   ……（此处省略1k字，没看懂怎么用语言模型的）

2. 如何预测agent's  behavier

会给每个agent 都预测多个path，planner可以根据这个信息来预防collision

在路口，一个车辆长时间停止（红色），我们会换道跟随刚刚停下的车辆，因为我们不知道为什么那辆车在那停那么久（可能是因为）



## auto labeling

一开始也是没有自动标注的，但是需要的标注数据到了一个体谅以后，我们觉得需要一个解决方案了



