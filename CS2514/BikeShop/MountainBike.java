/**
 * A class 'MountainBike' that encapsulates a mountain bike.
 * Instance variables include 'lowFrame'
 * 'MountainBike' is a subclass of 'Bike'
 *
 * @author: Eimear Foley 115352866
 */

public class MountainBike extends Bike {
	private static String lowFrame;
	
	// 'MountainBike' constructor
	public MountainBike(Object Frame, Object Brakes, Object Saddle, 
			Object Handlebar, Object Wheels) {
		// calls constructor from super class 'Bike'
		super(Brakes, Saddle, Handlebar, Wheels); 
		((Frame) Frame).setType("Low Frame");
		lowFrame = ((Frame) Frame).getType();
	}
	
	// Specialisation of 'Bike' printComponents() method
	@Override
	public void printComponents(){
		super.printComponents();
		System.out.printf(", " + lowFrame + ". %n");
	}

}
