### 0.前言

最近给树莓派安装了kali系统，想在闲余时间在树莓派上跑些脚本。ssh实时查看太麻烦，想到手头有OLED（SSD1306) 和几个RGB灯，便想着给树莓派做个实时显示系统，可以直观的查看到树莓派运行的状态。说干就干。

#### 0.1设计目标

- 开机自启动
- OLED实时显示树莓派运行信息
	- IP地址
	- CPU使用率
	- 内存大小与使用率
	- 硬盘大小与使用率
- RGB灯根据CPU的使用率变换颜色，由低到高为 绿->蓝->黄->红

#### 0.2 准备材料

- 安装好系统的树莓派3B+（我安装的是kali系统）
- RGB等一个
- SSD1306 128*32 OLED显示屏
- 杜邦线若干
- 热熔胶（真是个好东西），支架材料若干

#### 0.3 前期准备

- 树莓派安装kali系统   [不懂看这里](http:// https://htmonster.xyz/blog/post/raspberry_pi_kali "不懂看这里")
- kali系统打开i2c功能  [不懂看这里](https://htmonster.xyz/blog/post/kali_i2c/  "不懂看这里")
- python相关库安装 (pip 安装不成功 建议直接下载安装  python setup.py)

| 库名             | 作用                     | 下载地址                                                     |
| ---------------- | ------------------------ | ------------------------------------------------------------ |
| RPi.GPIO         | 树莓派的GPIO库 控制RGB灯 | https://sourceforge.net/projects/raspberry-gpio-python/files/latest/download |
| Adafruit-SSD1306 | ssd1306的使用库          | https://github.com/adafruit/Adafruit_Python_SSD1306.git      |
| psutil           | python 的性能查看工具    |                                                              |

#### 0.4 相关资料

##### GPIO接口图

![](http://images.htmonster.xyz/img/20191205/XbqFYS5N95P6.png?imageslim)


### 1. OLED显示信息

#### 1.1连接图

![]( http://images.htmonster.xyz/img/20191204/d3MKMasDFxiC.png?imageslim )

#### 1.2 编写OLED显示类

在github的example  https://github.com/adafruit/Adafruit_Python_SSD1306/tree/master/examples 里看到许多例子，其中的state.py与我设想的最类似。于是修改封装成OLED显示类 **ssd1306show.py**


#### 1.3 测试

使用python 启动 可以看到OLED屏幕显示，测试成功

```python ssd1306show.py ```

![](http://images.htmonster.xyz/img/20191205/1ngHmCEoyyB5.png?imageslim)

### 2.RGB灯显示状态

#### 2.1 连接图

![](http://images.htmonster.xyz/img/20191204/jVB8cISkpgBv.png?imageslim)

#### 2.1编写RGB 显示类

###### 注意事项：

注意GPIO的编码方式，分为BCM和Board两种 不同编码不同，我就在这里摔了一个坑。

#### 2.3 测试

python 启动文件 可以看到RGB 颜色变化 测试成功



### 3. 状态监控

状态监控使用了cmd命令与psutil相结合的方法。对于IP来说，变数不大，获取一次就行。其他的数据每隔一段时间获取。

psutil资料：https://www.liaoxuefeng.com/wiki/1016959663602400/1183565811281984

综合显示模块，写出综合模块 stateMonitor.py

经过测试可以实现，效果还不错，哈哈哈。

![](http://images.htmonster.xyz/img/20191205/jwBTownMi1ut.png?imageslim)



### 4.终极：设置开机启动

查阅了资料，设置开机启动的方法有三种：

1. /etc/init.d/
2. /etc/profile.d/
3. crontab定时脚本

经过本人测试，还是第3个有效，所以选择第三个。

#### 4.1 编写bash 允许脚本

```shell
python xxxx/xxx/stateMonitor.py&
```

- 路径使用绝对路径
- & 让python脚本后台允许

保存为run.sh

#### 4.2 修改crontab任务

1. 打开定时任务

```shell
crontab -e # 编辑
```

2. 添加定时任务

```shell
# For details see man 4 crontabs
# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed
@reboot  xxx/xxx/run.sh  #添加此条  路径为绝对路径
```

#### 4.3 开机重启即可




## 最终效果图
上一个最终效果图,用支架搭了一个手臂架，这样就可以随时调整方向，哈哈哈。

![](http://images.htmonster.xyz/img/20191205/Sci61RE2RUfu.png?imageslim)
