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
	
	public String login() throws Exception
	{
		if (getUsername().equals("chw"))
		{
			setTip("��ϲͨ��login()��¼�ɹ���");
			return SUCCESS;			
		}
			
		else
			return ERROR;
	}
	
	public String regist() throws Exception
	{
		setTip("��ϲͨ��regist()ע��ɹ���");
		return SUCCESS;		
	}
	
	
	public String execute() throws Exception
	{
		if (getUsername().equals("chw"))
			return SUCCESS;
		else
			return ERROR;
	}

}
