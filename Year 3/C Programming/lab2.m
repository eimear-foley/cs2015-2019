#import <Foundation/Foundation.h>
#include "math.h"

/*
 * Point interface
 */
@interface Point : NSObject
{
    int x;
    int y;
}
@property (assign) int x, y;
- (void) initSetX: (int) i andSetY: (int) j;
@end

/*
 * Point implementation
 */
@implementation Point
@synthesize x,y;
- (void) initSetX: (int) i andSetY: (int) j {
    x = i;
    y = j;
}
@end


/*
 * Circle interface
 */
@class Point;
@interface Circle: Point
{
    float radius;
    Point *origin;
}
@property float radius;
@property (nonatomic, retain) Point *origin;
-(float) area;
-(void) setRadius: (float) r;
-(void) setOrigin: (Point *) pt;
@end

/*
 * Circle implementation
 */
@implementation Circle
@synthesize radius, origin;
-(void) setOrigin: (Point *) pt{
    origin = pt;
}
-(void) setRadius: (float) r{
    radius = r;
}
-(float) area{
    return M_PI * pow(radius, 2);
}
@end

/*
 * Cylinder interface
 */
@interface Cylinder: Circle{
    float height;
    Circle *circle;
}
@property (assign) float height;
@property (nonatomic, retain) Circle *circle;
-(void) setHeight: (float) h;
-(float) volume;
@end

/*
 * Cylinder implementation
 */
@implementation Cylinder
@synthesize height, circle;
-(void) setHeight: (float) h{
    height = h;
}
-(float) volume{
    return height * [circle area];
}
@end

/*
 * Main function
 */
int main(int argc, const char * argv[]){
    NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];
    Point *pt = [[Point alloc] init];
    [pt initSetX: 2 andSetY: 3];
    NSLog(@"%i, %i", pt.x, pt.y);
    Circle *circle = [[Circle alloc] init];
    circle.origin = pt;
    [circle setRadius: 5];
    NSLog(@"%.2f", [circle area]);
    Cylinder *cylinder = [[Cylinder alloc] init];
    [cylinder setHeight: 7];
    cylinder.circle  = circle;
    NSLog(@"%.2f", [cylinder volume]);
    [pool drain];
    return 0;
}
