<%@ page contentType="text/html; charset=GBK" language="java" errorPage="" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<script type="text/javascript">
	function logintwo()
	{
		targetForm=document.forms[0];
		targetForm.action="loginPro";
		targetForm.submit();
	}
	function regist()
	{
		targetForm=document.forms[0];
		targetForm.action="registPro";
		targetForm.submit();
	}
</script>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>��¼ҳ��</title>
</head>
<body>

<form action="*Pro" method="post">
<table align="center">
	<caption><h3>ͨ���</h3></caption>
	
	<tr>
		<td>�û�����<input type="text" name="username"/></td>
	</tr>
	<tr align="center">
		<td>
			<input type="submit" value="��¼" onclick="logintwo();"/>
			<input type="button" value="ע��" onclick="regist();"/>									
		</td>			
	</tr>
</table>
</form>
</body>
</html>
