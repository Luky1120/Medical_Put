#include <Servo.h> 
 
int servoPin1 = 9;
int servoPin2 = 10;

Servo servo1;
Servo servo2;  

int angle1 = 0; 
int angle2 = 0;// servo position in degrees 
int step=45;
int sum=0;
const int speakerpin = 8; //스피커 부저 연결 핀
int sensor;

void setup() 
{ 
    Serial.begin(9600);
    servo1.attach(servoPin1); //servo1에 입출력 9번 핀을 지정
    servo2.attach(servoPin2);
    pinMode(speakerpin, OUTPUT);
} 


void loop() 
{ 
  sensor = analogRead(A0);
  // 센서가 움직이지 않을때는 센서 값이 1023입니다.
  if (sensor<4){
    for (int hz = 300; hz <= 750; hz++)
    {
      tone(speakerpin, hz);

      delay(5);
    }

    for (int hz = 750; hz >= 300; hz--)
    {
      tone(speakerpin, hz);

      delay(5);
    }
    Serial.print("Sensor Value: "); // 시리얼 모니터에 값을 보여줍니다.
    Serial.println(sensor);
    delay(100);
    noTone(speakerpin);
    delay(100);
    }
  
  


  if(Serial.available()>0)
  {
    char c;
    
    c = Serial.read();
    if(c == '1')
    {
      angle1 += step;
      servo1.write(angle1); 
      delay(15); 
        
        
      if(angle1 == 180){
        angle1=0;
        servo1.write(angle1); 
        delay(15); 
        } 
    }
    if(c == '2')
    {
      angle2 += step;
      servo2.write(angle2); 
      delay(15); 
        
        
      if(angle2 == 180){
        angle2=0;
        servo2.write(angle2); 
        delay(15);  
      }
    }
  }
} 
 
