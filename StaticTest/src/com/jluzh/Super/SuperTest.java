package com.jluzh.Super;

public class SuperTest {
	public int a=1;
	private int b=2;
	protected int c=3;
public SuperTest() {
	this("he");
	// TODO Auto-generated constructor stub
System.out.println("我是父类构造方法");
}
public SuperTest(String name) {
	
	System.out.println("我是父类有参构造方法"+name);
}
public void sup() {
	String a=super.toString();
	// TODO Auto-generated method stub
System.out.println("我是父类普通方法"+a);
}
public static void main(String[] args) {
SuperTest s=new SuperTest();
s.sup();

}
}
