Loading data...
###############
原始特征
Starting training...
[LightGBM] [Warning] Auto-choosing row-wise multi-threading, the overhead of testing was 0.003967 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[1]     valid_0's l2: 0.152605  valid_0's l1: 0.314806
Training until validation scores don't improve for 5 rounds
[2]     valid_0's l2: 0.143673  valid_0's l1: 0.305087
[3]     valid_0's l2: 0.135571  valid_0's l1: 0.295837
[4]     valid_0's l2: 0.128267  valid_0's l1: 0.287072
[5]     valid_0's l2: 0.121692  valid_0's l1: 0.278715
[6]     valid_0's l2: 0.115697  valid_0's l1: 0.270778
[7]     valid_0's l2: 0.110261  valid_0's l1: 0.263227
[8]     valid_0's l2: 0.105357  valid_0's l1: 0.25604
[9]     valid_0's l2: 0.10098   valid_0's l1: 0.249274
[10]    valid_0's l2: 0.097005  valid_0's l1: 0.242825
[11]    valid_0's l2: 0.0934305 valid_0's l1: 0.236692
[12]    valid_0's l2: 0.0901881 valid_0's l1: 0.230838
[13]    valid_0's l2: 0.0872509 valid_0's l1: 0.225265
[14]    valid_0's l2: 0.0846184 valid_0's l1: 0.220007
[15]    valid_0's l2: 0.0822431 valid_0's l1: 0.215
[16]    valid_0's l2: 0.0800657 valid_0's l1: 0.210212
[17]    valid_0's l2: 0.0781334 valid_0's l1: 0.205691
[18]    valid_0's l2: 0.0763833 valid_0's l1: 0.201373
[19]    valid_0's l2: 0.0748111 valid_0's l1: 0.197291
[20]    valid_0's l2: 0.0733904 valid_0's l1: 0.193428
Did not meet early stopping. Best iteration is:
[20]    valid_0's l2: 0.0733904 valid_0's l1: 0.193428
Saving model...
Starting validate...
The rmse of validate is: 0.27090664533077335
精确度： 0.9083
Starting predicting...
The rmse of prediction is: 0.27090664533077335
精确度： 0.91028
###############
添加一个衍生变量
Starting training...
[LightGBM] [Warning] Auto-choosing row-wise multi-threading, the overhead of testing was 0.003434 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[1]     valid_0's l2: 0.15261   valid_0's l1: 0.314812
Training until validation scores don't improve for 5 rounds
[2]     valid_0's l2: 0.143669  valid_0's l1: 0.305096
[3]     valid_0's l2: 0.135549  valid_0's l1: 0.295829
[4]     valid_0's l2: 0.128243  valid_0's l1: 0.28705
[5]     valid_0's l2: 0.121679  valid_0's l1: 0.278714
[6]     valid_0's l2: 0.115696  valid_0's l1: 0.270778
[7]     valid_0's l2: 0.110272  valid_0's l1: 0.263235
[8]     valid_0's l2: 0.105372  valid_0's l1: 0.256056
[9]     valid_0's l2: 0.100974  valid_0's l1: 0.249274
[10]    valid_0's l2: 0.0969849 valid_0's l1: 0.24281
[11]    valid_0's l2: 0.0934029 valid_0's l1: 0.236671
[12]    valid_0's l2: 0.0901532 valid_0's l1: 0.230819
[13]    valid_0's l2: 0.0872204 valid_0's l1: 0.225282
[14]    valid_0's l2: 0.08458   valid_0's l1: 0.220006
[15]    valid_0's l2: 0.0822079 valid_0's l1: 0.215003
[16]    valid_0's l2: 0.0800738 valid_0's l1: 0.210261
[17]    valid_0's l2: 0.078117  valid_0's l1: 0.205712
[18]    valid_0's l2: 0.0763486 valid_0's l1: 0.201378
[19]    valid_0's l2: 0.0747599 valid_0's l1: 0.197287
[20]    valid_0's l2: 0.0733232 valid_0's l1: 0.193396
Did not meet early stopping. Best iteration is:
[20]    valid_0's l2: 0.0733232 valid_0's l1: 0.193396
Saving model...
Starting validate...
The rmse of validate is: 0.27078251668400777
精确度： 0.9102
Starting predicting...
The rmse of prediction is: 0.27078251668400777
精确度： 0.9107

原始特征精确度为0.91028，添加一个衍生变量之后精确度为0.9107。精确度有略微提升。