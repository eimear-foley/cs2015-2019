import java.rmi.Remote;
import java.rmi.RemoteException;

public interface CalculatorInterface extends Remote { 
    public double add(double x, double y) 
        throws java.rmi.RemoteException; 
 
    public double sub(double x, double y) 
        throws java.rmi.RemoteException; 
 
    public double mul(double x, double y) 
        throws java.rmi.RemoteException; 
 
    public double div(double x, double y) 
        throws java.rmi.RemoteException; 
        
    public double pi()
        throws java.rmi.RemoteException;
}
