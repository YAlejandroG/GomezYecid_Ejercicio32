#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

double T = 40;
double rho = 0.001;
double Tmax = 6;
double dT = 0.01;
double Xmax = 1;
double dX = 0.01;
int Nt = Tmax/dT;
int Nx = Xmax/dX;

int ONDA(int Nt,int Nx,string nombre);

int main(){
    
    ONDA(Nt,Nx,"onda.dat");
    
    return 0;
}

int ONDA(int Nt,int Nx,string nombre){
    
    double x;
    
    double **Onda = new double *[Nt+1];
    for(int i=0;i<=Nt;i++){
        Onda[i] =new double[Nx+1];
    }

    for(int j=0;j<=Nj;j++){
        x = j*dX;
        if(j<=0.8*Xmax){
            Onda[0][j] = 1.25*x/Xmax;
        }
        else{
            Onda[0][j] = 5-5*x/Xmax;
        }
    }
    
    for(int i=1;i<=Nt;i++){
        Onda[i][0] = 0;
        Onda[i][Nx] = 0;
    }
    
    for(int i=0;i<Nt;i++){
        for(int j=1; j<Nx; j++){
            PSI[i+1][j] = PSI[i][j]+D*dT*(PSI[i][j+1]-2*PSI[i][j]+PSI[i][j-1])/pow(dX,2)+dT*S;
        }
    }
    
    ofstream outfile;
    outfile.open(nombre);
    
    double time = 0;
    
    for(int i=0; i<=Nt; i++){
        outfile<<time<<"\t";
        time += dT;
        for(int j=0; j<=Nx; j++){
            outfile<<PSI[i][j]<<"\t";
        }
        outfile<<endl;
    }
    
    double x = -1;
    outfile<<0<<"\t";
    for(int j=0; j<=Nx; j++){
        outfile<<x<<"\t";
        x += dX;
    }
    outfile.close();
    
    return 0;
}
