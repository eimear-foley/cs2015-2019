import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class Server implements CalculatorInterface {
    public Server() throws java.rmi.RemoteException { 
        super(); 
    } 

    public double add(double x, double y) throws java.rmi.RemoteException { 
        return x + y; 
    } 

    public double sub(double x, double y) throws java.rmi.RemoteException { 
        return x - y; 
    } 

    public double mul(double x, double y) throws java.rmi.RemoteException { 
        return x * y; 
    } 

    public double div(double x, double y) throws java.rmi.RemoteException { 
        return x / y; 
    }

    public double pi() throws java.rmi.RemoteException { 
        return 3.14159265359;
    }

    public static void main(String args[]) {
        try {
            Server obj = new Server();
            CalculatorInterface stub = (CalculatorInterface)UnicastRemoteObject.exportObject(obj, 0);
            // Bind the remote object's stub in the registry
            Registry registry = LocateRegistry.getRegistry();
            registry.bind("Calculator", stub);
            System.err.println("Server ready"); 
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
        }       
    }
}