/**
 * A class 'Hybrid' encapsulates a hybrid bike.
 * Instance variables include 'mediumFrame'
 * Sub class of intermediate class 'BikeWithLights'
 *
 * @author: Eimear Foley 115352866
 */

public class Hybrid extends BikeWithLights {
	private static Object mediumFrame;
	
	// 'Hybrid' constructor
	public Hybrid(Object Brakes, Object Saddle, Object Handlebar,
			Object Wheels, Object Front, Object Rear, Object Frame) {
		// calls constructor from intermediate class 'BikeWithLights'
		super(Brakes, Saddle, Handlebar, Wheels, Front, Rear);
		((Frame) Frame).setType("Medium Frame");
		mediumFrame = ((Frame) Frame).getType();
	}
	
	// Specialization of 'BikeWithLights' printComponents() method
	@Override
	public void printComponents(){
		super.printComponents();
		System.out.printf(", " + mediumFrame + ". %n");
	}

	

}
