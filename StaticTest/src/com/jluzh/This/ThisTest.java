package com.jluzh.This;

public class ThisTest {
public ThisTest(){
	this("����");
	System.out.println("�����޲ι���");
}
public ThisTest(String name) {
	System.out.println("��ã�"+name);
}
public void haha() {
	this.toString();
}
public static void main(String[] args) {
	ThisTest t=new ThisTest();
	t.toString();
	t.haha();
}
}
