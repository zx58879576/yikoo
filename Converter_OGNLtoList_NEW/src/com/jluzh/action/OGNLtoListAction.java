package com.jluzh.action;

import java.util.List;

import com.opensymphony.xwork2.ActionSupport;

public class OGNLtoListAction extends ActionSupport{
	private List<User> user;

	public List<User> getUser() {
		return user;
	}

	public void setUser(List<User> user) {
		this.user = user;
	}
	
	@Override
	public String execute() throws Exception {
		// TODO Auto-generated method stub
		if(getUser().get(1).getName().equals("chw"))
		{
			user.get(1).setAge(user.get(1).getAge()+10);
			return SUCCESS;
		}
		else
			return ERROR;
	}
}
