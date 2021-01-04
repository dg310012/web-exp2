### 1.运行环境
 Ubuntu 20.04.1 LTS


### 2.运行步骤

+ 安装必要依赖
```
    cd src
    pip install -r requirements.txt
```

+ 构建代码
```
    python setup.py develop
```

+ 执行预处理程序，根据提供的test.txt和train.txt生成mytest.txt、mytrain.txt和myverify.txt。
```
    cd code
    python prepare.py
```

+ 执行程序，生成result.txt（用数字0-9来表示关系）
```
    python train_supervised_cnn.py --train_file mytrain.txt --val_file myverify.txt --test_file mytest.txt --rel2id_file myjson.json
```

+ 将result.txt转化为relationshipResult.txt来得到最终结果
```
    python transformResult.py
```
