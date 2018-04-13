package com.jluzh.This;

public class ThisTest {
public ThisTest(){
	this("钟翔");
	System.out.println("我是无参构造");
}
public ThisTest(String name) {
	System.out.println("你好："+name);
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
