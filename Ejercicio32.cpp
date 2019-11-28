#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

double Tension = 40;
double rho = 0.01;
double C = pow(Tension/rho,0.5);
double Tmax = 0.1;
double dT = 0.0001;
double Xmax = 1;
double dX = 0.01;
double Cprima = dX/dT;
int Nt = Tmax/dT;
int Nx = Xmax/dX;

int ONDA(int Nt,int Nx,string nombre);

int main(){
    
    ONDA(Nt,Nx,"onda.dat");
    
    return 0;
}

int ONDA(int Nt,int Nx,string nombre){
    
    double x;
    
    double Onda[Nt+1][Nx+1];

    for(int j=0;j<=Nx;j++){
        x = j*dX;
        Onda[0][j] = pow(10,-4)*sin(2*M_PI*x/Xmax);
    }
    
    for(int i=1;i<=Nt;i++){
        Onda[i][0] = 0;
        Onda[i][Nx] = 0;
    }
    
    for(int j=1;j<Nx;j++){
        Onda[1][j] = Onda[0][j]+pow(C/Cprima,2)*(Onda[0][j+1]+Onda[0][j-1]-2*Onda[0][j])/2;
    }
    
    for(int i=1;i<Nt;i++){
        for(int j=1; j<Nx; j++){
            Onda[i+1][j] = 2*Onda[i][j]-Onda[i-1][j]+pow(C/Cprima,2)*(Onda[i][j+1]+Onda[i][j-1]-2*Onda[i][j]);
        }
    }
    
    ofstream outfile;
    outfile.open(nombre);
    
    for(int i=0; i<=Nt; i++){
        for(int j=0; j<=Nx; j++){
            outfile<<Onda[i][j]<<"\t";
        }
        outfile<<endl;
    }
    outfile.close();
    
    return 0;
}
