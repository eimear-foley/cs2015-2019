using System;

public class Point {
    private int x; 
    private int y;
    
    public int X{
        get{
            return x;
        }
        set{
            x = value;
        }
    }
    
    public int Y{
        get{
            return y;
        }
        set{
            y = value;
        }
    }

    public Point(int i, int j){
        x = i;
        y = j;
    }
}

public class Circle : Point{
    private float radius;
    public Point origin; 
    
    public float Radius{
        get{
            return radius;
        }
        set{
            radius = value;
        }
    }
    
    public Circle(int i, int j, float r): base(i, j){
        radius = r;
    }

    public void setOrigin(Point pt){
        origin = pt; 
    }

    public float area(){
        float pi = (float) Math.PI;
        float power = (float) Math.Pow(radius, 2);
        return pi *  power;
    }
}

public class Cylinder : Circle{
    private float height;
    
    public float Height{
        get{
            return height;
        }
        set{
            height = value;
        }
    }
    
    public Cylinder(int i, int j, float r, float h): base(i,j,r){
        height = h;
    }

    public float volume(){
        return height * base.area(); 
    }
}

public class Test{
    public static void Main(){
        Point point = new Point(2, 3);
        Console.WriteLine("Point: {0},{1}", point.X, point.Y);
        Circle circle = new Circle(2,3,5);
        Console.WriteLine("Radius: {0}", circle.Radius);
        circle.origin = point; 
        Console.WriteLine("Area: {0}", circle.area());
        Cylinder cylinder = new Cylinder(2,3,5,7);
        Console.WriteLine("Height: {0}", cylinder.Height);
        Console.WriteLine("Volume: {0}", cylinder.volume());
    }
}
