<?php

	if(isset($_POST['FunCode']) && $_POST['FunCode']== '4000'){ //轮询请求
		echo outPro(); //调用出货请求
	}elseif (isset($_GET['new_pro'])) { //添加新的出货请求
		$rand_filename = './products/'.rand(1000000,9999999);
		file_put_contents($rand_filename, $_GET['new_pro']);
	}
	function outPro(){ //从products 目录 取出一个文件 读文件中的货道号并出货，出完货删除对应文件
		$files = scandir("./products/");
		foreach ($files as $file) {
			if(count($files) == 2){
				$info = '{ "Status": "0","MsgType":"3",Err":"暂无任务"}';
				break;
			}
			if($file !== "." && $file !== ".."){
				$pro = "./products/".$file;
				$pro_id = file_get_contents($pro);
				unlink($pro);
				$TradeNo = date('YmdHis', time()).get_millisecond();
				$info = '{ "Status": "0","MsgType":"0","TradeNo":"'.$TradeNo.'","SlotNo":"'.$pro_id.'","ProductID":"0","Err":"成功"}';
				break;
			}
		}
		return $info;
	}
	function get_millisecond(){  //生成一个时间用作订单号

	    list($usec, $sec) = explode(" ", microtime());   

	    $msec=round($usec*1000);  

	    return $msec;

	}
?>
