package com.jluzh.action;

import com.opensymphony.xwork2.ActionSupport;

public class loginAction extends ActionSupport
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
	
	public String execute() throws Exception
	{
		if (getUsername().equals("chw"))
			return SUCCESS;
		else
			return ERROR;
	}

}
