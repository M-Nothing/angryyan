window.onload = function(){
	var err = document.getElementsByClassName("err")[0];
	var name = document.getElementsByName('name')[0];
	var pwd = document.getElementsByName('pwd')[0];
	function vaildName(){
		if(name.value == ''){
			err.style.display = 'block';
			err.className = 'err';
			err.innerHTML = '用户名不能为空';
			name.style.border = '1px solid red';
		}
		else {
			if(name.value.length>10){
				err.style.display = 'block';
				err.className = 'err';
				err.innerHTML = '用户名不能超过10位';
				name.style.border = '1px solid red';
			}
			else{
				var parten = /^[\\u4E00-\\u9FA5\\uF900-\\uFA2D\\w]$/;
				if(parten.test(name.value)){
					err.style.display = 'block';
					err.className = 'err';
					err.innerHTML = '用户名不能包含特殊字符';
					name.style.border = '1px solid red';
				}else{
					err.style.display = 'block';
					err.className = 'ok';
					err.innerHTML = '用户名正确';
					name.style.border = 'none';
				}
			}
		}
	}
	function vaildPwd(){
		if(pwd.value == ''){
			err.style.display = 'block';
			err.className = 'err';
			err.innerHTML = '密码不能为空';
			pwd.style.border = '1px solid red';
		}
		else 
		{
			var parten = /^[A-Za-z0-9]{6,20}$/;
			if(!parten.test(pwd.value)){
				err.style.display = 'block';
				err.className = 'err';
				err.innerHTML = '密码为6-20位数字和字母的组合';
				pwd.style.border = '1px solid red';
			}else{
				err.style.display = 'block';
				err.className = 'ok';
				pwd.style.border = 'none';
				err.innerHTML = '密码正确';
			}
	    }
	}
	name.onfocus = function(){
		name.style.border = 'none';
		err.style.display = 'none';
	}
	name.onfocus = function(){
		pwd.style.border = 'none';
		err.style.display = 'none';
	}
	name.onblur = function(){
		vaildName();
	}
	pwd.onblur = function(){
		vaildPwd();
	}
}()