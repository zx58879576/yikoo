<%@ page contentType="text/html; charset=GBK" language="java" errorPage="" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>登录页面</title>
</head>
<body>

<form action="login1" method="post">
<table align="center">
	<caption><h3>用户页面</h3></caption>
	<tr>
		<td>年龄(整&nbsp;&nbsp;型)：<input type="text" name="age"/></td>		
	</tr>
	<tr>
		<td>密码(双精度)：<input type="text" name="password"/></td>		
	</tr>
	<tr>
		<td>生日(日&nbsp;&nbsp;期)：<input type="text" name="birth"/></td>		
	</tr>
		
	<tr align="center">
		<td><input type="submit" value="登录"/>
			<input type="reset" value="重填" />			
		</td>
			
	</tr>
</table>
</form>
</body>
</html>
