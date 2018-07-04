<%@ page contentType="text/html; charset=GBK" language="java" errorPage="" %>
<%@taglib prefix="s" uri="/struts-tags"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>登录页面</title>
</head>
<body>

<form action="login1" method="post">
<table align="center">
	<caption><h3>使用OGNL转换为List集合</h3></caption>
	
	<tr>
		<td>用户1的用户名：<input type="text" name="user[0].name"/></td>
	</tr>
	<tr>
		<td>用户1的年&nbsp;&nbsp;龄：<input type="text" name="user[0].age"/></td>
	</tr>
	<tr>
		<td>用户2的用户名：<input type="text" name="user[1].name"/></td>
	</tr>
	<tr>
		<td>用户2的年&nbsp;&nbsp;龄：<input type="text" name="user[1].age"/></td>
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
