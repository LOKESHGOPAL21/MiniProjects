package dao;

import java.util.List;

import beans.Register;
import beans.Task;

public interface ToDoDAOIntf {
	public abstract int register(Register register);
	int login(String email,String pass);
	public int addTask(int regId,Task task);
	public List<Task> findAllTasksByRegId(int regId);
	public boolean markTaskCompleted(int regId, int taskId);
	public String getFnameByRegId(int regId);
}
/*
 * In java interface all 
 * 	variables are public static final by default and
 * 	methods are public abstract by default
 * */
