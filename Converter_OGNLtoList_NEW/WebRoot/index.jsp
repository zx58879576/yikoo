<%@ page contentType="text/html; charset=GBK" language="java" errorPage="" %>
<%@taglib prefix="s" uri="/struts-tags"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>��¼ҳ��</title>
</head>
<body>

<form action="login1" method="post">
<table align="center">
	<caption><h3>ʹ��OGNLת��ΪList����</h3></caption>
	
	<tr>
		<td>�û�1���û�����<input type="text" name="user[0].name"/></td>
	</tr>
	<tr>
		<td>�û�1����&nbsp;&nbsp;�䣺<input type="text" name="user[0].age"/></td>
	</tr>
	<tr>
		<td>�û�2���û�����<input type="text" name="user[1].name"/></td>
	</tr>
	<tr>
		<td>�û�2����&nbsp;&nbsp;�䣺<input type="text" name="user[1].age"/></td>
	</tr>
	<tr align="center">
		<td><input type="submit" value="��¼"/>
			<input type="reset" value="����" />			
		</td>
			
	</tr>
</table>
</form>
</body>
</html>
