package com.jluzh.action;

import com.opensymphony.xwork2.ActionSupport;

public class LoginRegistAction extends ActionSupport
{
	private String username;
	private String tip;
		
	public String getUsername()
	{
		return username;
	}
	public void setUsername(String username)
	{
		this.username=username;
	}
	
	public String getTip()
	{
		return tip;
	}
	public void setTip(String tip)
	{
		this.tip=tip;
	}
	
	
	public String regist() throws Exception
	{
		setTip("��ϲ��ע��ɹ�!");
		return SUCCESS;
	}
	
	public String loginthree() throws Exception
	{
		if (getUsername().equals("chw"))
		{
			setTip("��ϲ����½�ɹ���three");
			return SUCCESS;
		}	
			
		else
			return ERROR;
	}
	public String execute() throws Exception
	{
		if (getUsername().equals("chw"))
		{
			setTip("execute");
			return SUCCESS;
		}	
			
		else
			return ERROR;
	}
}
