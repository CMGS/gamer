Gamer
==============

游戏玩家永不为奴！

```
pip install -r requirements.txt
python go.py
```

不要用 [vpost](https://vpost.com/) 和 [buyandship](https://www.buyandship.com.sg/) 地址，黑名单了，一定会砍单。

NV 商店利用地址和邮箱做唯一性验证，所以重复邮箱，砍单，重复地址，砍单。名字一样无所谓，信用卡一样无所谓。

中国信用卡不一定能用，某张招行双币砍单了。

修改 `common.py` 里面的地址，姓名等内容，注意 `Month`只支持单位数字，`01` 就写 `1`，`12` 可以写 `12`。

可以使用 4070 的地址跑整个流程测试。

没有提示音，可以跑在后台，如果有卡会第一时间跳转到最后的 `review order` 步骤，不过你需要自己点下 anti bot 验证，理论上只要页面结构不变 5090 也可以下单。

```
mv config.yaml.sample config.yaml
```

然后修改信息