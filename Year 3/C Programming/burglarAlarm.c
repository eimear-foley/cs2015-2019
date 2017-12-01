/**
 * Burglar Alarm Project 2017
 * Language: C
 * Hardware: Arduino Duemilanove
 */

#include <LiquidCrystal.h> //LCD library
#include <EEPROM.h> //EEPROM memory library
#include <IRremote.h> //Infrared Remote library

//Define buttons of IR remote
#define  IR_0       0xff6897
#define  IR_1       0xff30cf
#define  IR_2       0xff18e7
#define  IR_3       0xff7a85
#define  IR_4       0xff10ef
#define  IR_5       0xff38c7
#define  IR_6       0xff5aa5
#define  IR_7       0xff42bd
#define  IR_8       0xff4ab5
#define  IR_9       0xff52ad
#define  IR_MINUS   0xffe01f
#define  IR_PLUS    0xffa857
#define  IR_EQ      0xff906f
#define  IR_ON_OFF  0xffa25d
#define  IR_MODE    0xff629d
#define  IR_MUTE    0xffe21d
#define  IR_PLAY    0xffc23d
#define  IR_REW     0xff22dd
#define  IR_FF      0xff02fd

//Initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

int PASS[4] = {1,2,3,4}; //Preset password for 'Enter/Exit' alarm zone
int buzzer = 8; // Buzzer connected to pin 8

//Time variables
byte volatile h; //Hours
byte volatile m; //Minutes
byte volatile s; //Seconds

// zone pins
int RECV_PIN = 7; //Data from IR remote received through IR sensor on pin 7
int cont = 9; //Pin 9 for 'Continuous Monitoring' alarm zone
int entry_pin = 10; //Pin 10 for 'Entry/Exit' zone
int analogue_pin = 6; //Pin 6 for 'Analogue' alarm zone
int dig_pin = 13; //Pin 13 for 'Digital' alarm zone

//Decoding results from IR Sensor
IRrecv irrecv(RECV_PIN);
decode_results results;

boolean prev_state = LOW; //Previous state of 'Analogue' alarm zone switch
int threshold = 5; //Threshold value for 'Analogue' alarm zone
int count = 0;
boolean dig_trigger = LOW; //'Digital' alarm zone's state initialied to LOW

/**
 * User must enter password for 'Entry/Exit' zone in 'countdown' seconds
 * Interrupts used for countdown
 */
boolean startcountdown = false; //Set to true when countdown has started
int countdown = 60; //Initialized to 60 seconds
int countdown_value = 60;

/**
 * Array of strings referencing 4 alarm zones
 * Used by 'showLastAlarm()' to print zone that was last activated to user
 */
String dests[4] = {"Entry/Exit", "Continuous", "Analogue", "Digital"};

/**
 * 'setup' function
 * - set up LCD, buzzer and 'Entry/Exit' alarm zone switch
 * - set up interrupts
 * - set up IR sensor to receive data
 */
void setup() {
  //Set up the LCD's number of columns and rows: 
  lcd.begin(16, 2);
  //Set buzzer up
  pinMode(buzzer, OUTPUT);
  //Set 'Entry/Exit' alarm zone switch up
  pinMode(entry_pin, INPUT);
  
  /**
   * Interrupts used for displayTime function
   */
  cli(); //Disable global interrupts
  TCCR1A = 0;
  TCCR1B = 0;
  OCR1A = 15625; //Set the count corresponding to 1 second
  TCCR1B |= (1 << WGM12); //Turn on CTC mode
  TCCR1B |= (1 << CS10);
  TCCR1B |= (1 << CS12); //Prescale at 1024
  TIMSK1 |= (1<< OCIE1A); //Enable CTC interrupt
  sei(); //Enable Global Interrupts

  /**
   * Initialise IR Sensor
   */
  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver
  
}

/**
 * Interpret data received from IR Remote
 */
int keyToInt(int key_pressed){
  switch(key_pressed){
    case IR_0: return 0;
    case IR_1: return 1;
    case IR_2: return 2;
    case IR_3: return 3;
    case IR_4: return 4;
    case IR_5: return 5;
    case IR_6: return 6;                                         
    case IR_7: return 7;  
    case IR_8: return 8;    
    case IR_9: return 9; 
    case IR_MINUS: return 10;  
    case IR_PLUS: return 11;   
    case IR_EQ: return 12;     
    case IR_ON_OFF: return 13;     
    case IR_MODE: return 14;   
    case IR_MUTE: return 15; 
    case IR_PLAY: return 16;   
    case IR_REW: return 17;  
    case IR_FF: return 18; 
    default: return -1;     
  }
}

/**
 * Sound alarm 
 * Write alarm time and zone to EEPROM in bytes
 */
void Alarm(byte dest){
  int addr = 0;
  EEPROM.write(addr, h);
  EEPROM.write(addr+1, m);
  EEPROM.write(addr+2, s);
  //Alarm zone written in bytes, interpreted later by 'showLastAlarm()' using 'dests[]'
  EEPROM.write(addr+3, dest); 
  
  int freq = 1911;
  for (int j =0; j< 10; j++){
    for (int i = 0; i < 100; i++){
      digitalWrite(buzzer, HIGH); 
      delayMicroseconds(freq);               
      digitalWrite(buzzer, LOW);    
      delayMicroseconds(freq); 
      }
    delay(25);
  }
  return;
}

/**
 * Time logic using interrupts
 */
ISR (TIMER1_COMPA_vect){
  s++;
  if(s==60){ 
    s=0; 
    m=m+1; 
  } 
  if(m==60){ 
    m=0; 
    h=h+1; 
  } 
  if(h==24){ 
    h=0; 
  } 
  if (startcountdown){
    countdown--;
  }
}


/**
 * Allow user to set time using IR remote
 */
void setTime(){
  lcd.clear();
  irrecv.resume();
  int i = 0;
  int time[6];
  while (i < 6){
    if (irrecv.decode(&results)) {
       if (keyToInt(results.value) != -1){
          time[i] = keyToInt(results.value);
          lcd.print(keyToInt(results.value));
          i++;
          if (i % 2 ==0){
            lcd.print(":");
          }
        }
        irrecv.resume();
     }
  }  
  h = time[0]*10 + time[1];
  m = time[2]*10 + time[3];
  s = time[4]*10 + time[5];
}


/**
 * Allow user to set 'Entry/Exit' alarm zone password
 */
void setPassword(){
  lcd.clear();
  int i = 0;
  irrecv.resume();
  while (i < 4){
     if (irrecv.decode(&results)) {
        if (keyToInt(results.value) != -1){
          lcd.print(keyToInt(results.value));
          PASS[i] = keyToInt(results.value);
          i++;
        }
    irrecv.resume();
    }  
  }
  lcd.clear();
  lcd.print("New password: ");
  lcd.setCursor(0,1);
  lcd.print(PASS[0]);
  lcd.print(PASS[1]);
  lcd.print(PASS[2]);
  lcd.print(PASS[3]);
  delay(1000);
  return;
}


/**
 * Allow user to set 'Digital' alarm zone state
 */
void setDigitalAlarm(){
  irrecv.resume();
  lcd.clear();
  while (true){
     if (irrecv.decode(&results)) {
        if (keyToInt(results.value) != -1){
           // If 0 entered, digital alarm will be triggered by LOW state
           if (keyToInt(results.value) == 0){
              dig_trigger = LOW;
              lcd.print("Set to LOW");
              delay(1000);
              return;
            }
            // If 1 entered, digital alarm will be triggered by HIGH state
            if (keyToInt(results.value) == 1){
               dig_trigger = HIGH;
               lcd.print("Set to HIGH");
               delay(1000);
               return;
            }
          }
          irrecv.resume();
      }
  }
}

// Sets value of the threshold for Analogue Alarm
void setThreshold(){
  lcd.clear();
  irrecv.resume();
  lcd.print("Set: ");
  while (true){
     if (irrecv.decode(&results)) {
          if (keyToInt(results.value) != -1){
              threshold = keyToInt(results.value);
              lcd.print(threshold);
              delay(500);
              lcd.clear();
              lcd.print("New threshold: ");
              lcd.setCursor(0,1);
              lcd.print(keyToInt(results.value));
              delay(1000);
              return;
          }
          irrecv.resume();
      }
  }
}

/**
 * Set 'Entry/Exit' time to enter or exit 'house'
 * In 'countdown' seconds
 */
void setEntryTime(){
  lcd.clear();
  irrecv.resume();
  lcd.print("Set: ");
  lcd.setCursor(0,1);
  countdown_value = 0;
  while (true){
     if (irrecv.decode(&results)) {
        if (keyToInt(results.value) != -1){
           if (keyToInt(results.value) == 16){
              countdown = countdown_value;
              return;
           }
           else {
              countdown_value = countdown_value*10 + keyToInt(results.value);
              lcd.print(keyToInt(results.value));
           }
        } irrecv.resume();
     }
  }
}

/**
 * Display the last time and alarm zone when 'Alarm()' was run on the LCD
 */
void showLastAlarm(){
  int addr = 0;
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("TIME");
  
  //Read alarm time from EEPROM
  while (addr < 3){
    lcd.print(":");
    byte digit = EEPROM.read(addr);
    if (digit < 10) {
      lcd.print("0"); 
    }
    lcd.print(digit);
    addr++; 
  }
  lcd.setCursor(0,1);
  lcd.print("ALARM @ ");
  //Read alarm zone from EEPROM and interpret using 'dest[]'
  lcd.print(dests[EEPROM.read(addr)]);
  delay(5000);
}

/**
 * Menu option for user to navigate through using IR remote
 * Allows user to:
 * - Reset digital time display
 * - Reset 'Entry/Exit' password
 * - Reset 'Digital' alarm zone state
 * - Reset 'Analogue' alarm zone threshold
 * - Reset 'Entry/Exit' time
 * - Display when alarm was last activated
 */
void Menu(){
  irrecv.resume();
  lcd.clear();
  String modes[6] = {"< Set Time >", "< Set Password >", "< Set Digital >", "< Set Thresh. >", "< Set EntryTime >", "< Last Alarm >"};
  int i = 0;
  while (true) {
     lcd.setCursor(0,0);
     lcd.print("Menu:");
     lcd.setCursor(0,1);
     lcd.print(modes[i]);
     if (irrecv.decode(&results)) {
        if (keyToInt(results.value) != -1){
           // If user presses mode button, exit menu.
           if (keyToInt(results.value) == 14){
              lcd.clear();
              return;     
           }
           //If user presses play/pause button, enter mode input.
           if (keyToInt(results.value) == 16){
              if (i == 0){
                 setTime();
              }
              if (i == 1){
                 setPassword();
               }
               if (i == 2){
                  setDigitalAlarm();
               }
               if (i == 3){
                  setThreshold();
               }
               if (i == 4){
                  setEntryTime();
               }
               if (i == 5){
                  showLastAlarm();
               }
               lcd.clear();
               return;
            }
            // If user presses fast forward key, go to next mode option
            if (keyToInt(results.value) == 18){
               i ++;
               lcd.clear();
               //Allow wraparound of menu options
               if (i == 6){
                  i = 0;
               }
             }
             // If user presses rewind key, go to previous mode option
             if (keyToInt(results.value) == 17){
                 //Allow wraparound of menu options
                 if (i == 0){
                    i = 5;
                 } else {
                    i --;
                 }
                 lcd.clear();
             }  
      }
      irrecv.resume();
    }
  }
}

/**
 * Display digital time to LCD
 * Initialised to 00:00:00 until user sets time
 */
void digitalTimeDisplay(){
  lcd.setCursor(0,0); 
  lcd.print("TIME:");
  
  //If single-digit, print an extra 0.
  if (h < 10){
    lcd.print("0");
  } 
  lcd.print(h);
  
  lcd.print(":");
  if (m < 10){
  lcd.print("0"); 
  }
  lcd.print(m);
  
  lcd.print(":");
  if (s < 10){
   lcd.print("0");
  } 
  lcd.print(s);  
}

/**
 * 'Entry/Exit' alarm zone condition activated
 * Use IR remote to enter correct password in 'countdown' seconds
 * Otherwise the alarm is sounded
 */
void entryExit(){
  lcd.clear();
  startcountdown = true; //Begin countdown to alarm.
  boolean keyPressed = false;
  byte dest = 0; //Used to write alarm zone to EEPROM
  int i = 0;
  while (countdown > 0){
    lcd.setCursor(0, 0);
    lcd.print("Enter Password:");
    if (irrecv.decode(&results)) {
      if (keyToInt(results.value) != -1){
        keyPressed = true;
         lcd.setCursor(0,1);
         //If incorrect digit entered at any time, run 'Alarm()'
         if (PASS[i] != keyToInt(results.value)){
           lcd.clear();
           lcd.print("Intruder!");
           Alarm(dest);
           lcd.clear();
           irrecv.resume();
           //Alarm sounded, end countdown
           startcountdown = false;
           countdown = countdown_value;
           return;
         }
         i++;
         lcd.print(keyToInt(results.value));
      }
      irrecv.resume();
      if (i >= 4){
        break;
      }
    }
  }
  
  startcountdown = false;
  countdown = countdown_value;
  
  //If countdown ended and password not fully entered:
  if (!keyPressed || i<4){
   lcd.clear();
   lcd.print("Intruder!");
   Alarm(dest);
   lcd.clear();
   return;
  }
  
  //If password correctly entered:
  delay(500);
  lcd.clear();
  lcd.print("Welcome Home");
  delay(1000);
  lcd.clear();
}

/**
 * 'Continuouse Monitoring' alarm zone activated
 * Represents a LOW to HIGH transition
 */
void continuousMonitoring(){
  byte dest = 1; //Used to write alarm zone to EEPROM
  lcd.clear();
  lcd.print("Intruder!");
  Alarm(dest);
  lcd.clear();
  return;
}

/**
 * 'Analogue' alarm zone activated
 */
void analogue(){
  byte dest = 2; //Used to write alarm zone to EEPROM
  lcd.clear();
  lcd.print("Intruder!");
  Alarm(dest);
  lcd.clear();
  return;
}

/**
 * 'Digital' alarm zone activated
 */
void digital(){
  byte dest = 3; //Used to write alarm zone to EEPROM
  lcd.clear();
  lcd.print("Intruder!");
  Alarm(dest);
  lcd.clear();
  return;
}

/**
 * Main function 
 */
void loop() {
  // display time
  digitalTimeDisplay();
  
  //If mode button pressed, enter menu
  if (irrecv.decode(&results)) {
     if (keyToInt(results.value) != -1){
       if (keyToInt(results.value) == 14){
         Menu();
       }
     }
   irrecv.resume();  
  }

  //If 'Entry/Exit' alarm zone state changed
  if (digitalRead(entry_pin) == HIGH){
    entryExit();
  }
  
  //If 'Continuous Monitoring' alarm zone state changed
  if (digitalRead(cont) == HIGH){
    continuousMonitoring();
  }
  
  // If 'Digital'alarm zone state is changed
  if (digitalRead(dig_pin) == dig_trigger){
     digital();
  }
  
  // When 'Analogue' alarm zone button is hit 'threshold' times, Alarm() is run.
  if (digitalRead(analogue_pin) != prev_state){
      prev_state = digitalRead(analogue_pin);
      count ++;
   }
   if (count == threshold * 2){
      analogue();
      count = 0;
   }

}
