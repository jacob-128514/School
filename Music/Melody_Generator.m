%creates a pseudo random chord progression with a melody line

clc;
clear;

%setting amplitude and frequency and note duration
amp=1.3;
fs=20500;  
duration=0.75;
freq=440;
t=0:1/fs:duration;
t1=0:1/fs:0.6;

n0 = 0;
n1 = 0;
n2 = 4;
n3 = n2 + 3;
n4 = n3 + 5;

for i = 1:4

a1=amp*sin(2^(n1/12)*8*freq*t);
a2=amp*sin(2^(n2/12)*8*freq*t);
a3=amp*sin(2^(n3/12)*8*freq*t);
a4=amp*sin(2^(n4/12)*8*freq*t);

%play chord
sound(a1);
sound(a2);
sound(a3);
sound(a4);

for k = 1:2
    
    %play melody (4 notes per chord change)
    a0=2*sin(2^(n0/12)*16*freq*t1);
    a5=0.7*sin(2*2^(n0/12)*16*freq*t1);
    a6=0.1*sin(2*2*2^(n0/12)*16*freq*t1);
    sound(a0);
    sound(a5);
    sound(a6);
    
    pause(0.8);
    if i == 4
        n0 = 0;
    else
    n0 = n0 + 2*randi([-1,1],1);
    end
    k = k+1;
    
end

%Choosing notes for the next chord
%I can't remember what the logic behind this was
if i == 7 || i == 3
    n1 = 0;
    n2 = randi([3,4],1);
    n3 = 7;
    n4 = 12;
else
    n1 = 0;
    n2 = randi([3,6],1);
end
    
if n2 == 3
    n3 = randi([6,7],1);
    n4 = randi([9,12],1);
else
    n3 = n2 + randi([3,5],1);
    n4 = n3 + randi([3,6],1);
end

n0 = n2;

i = i + 1;

%Let the beautiful music wash over you
end
