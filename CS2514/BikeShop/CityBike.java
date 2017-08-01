/**
 * A class 'CityBike' which encapsulates a city bike.
 * Instance variables includes 'frame', 'carrier'
 * Sub class of intermediate class 'BikeWithLights'
 *
 * @author: Eimear Foley 115352866
 */
 
public class CityBike extends BikeWithLights {
    private static String frame; 
    private static String carrier; 
     
    // 'CityBike' constructor
    public CityBike(Object Brakes, Object Saddle, Object Handlebar,
            Object Wheels, Light light1, Light light2, 
            Object Frame, Object Carrier ) {
        // calls constructor from intermediate class 'BikeWithLights'
        super(Brakes, Saddle, Handlebar, Wheels, light1, light2);
        ((Frame) Frame).setType("High Frame");
        frame = ((Frame) Frame).getType();
        carrier = ((Carrier) Carrier).getType();
    }
     
     
    // Specialization of 'BikeWithLights' printComponents() method
    @Override
    public void printComponents(){
        super.printComponents();
        System.out.printf(", " + frame + ", " + carrier + ". %n");
    }
 
}
