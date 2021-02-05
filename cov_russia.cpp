#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <cassert>
#include "spline.h"
using namespace std;

const double tau = 0.01;
const double h = 0.02;
const double xmax = 6.5; // Moscow -- Anadir: 6212 km
const size_t x_size = xmax / h + 1;
double u = 0.087; // thousands of km
double T = 0; 
double sigma1 = 0;

vector<double> dens_x {0, 0.5, .7, 1.16, 1.85, 2.150, 2.5, 3.6, 6};
vector<double> dens_y {434.63, 28.77, 16, 14.1, 11.26, 4.53, 3, 1.67, 3.08};

tk::spline n1;

double sigma(double x) { return sigma1 * n1(x); }

int main(int argc, char** argv)
{
	double scale = 1;
	for(int i = 1; i < argc; ++i)
	{
		string opt(argv[i]);
		auto index = opt.find('=');
		if(index != string::npos) opt[index] = ' ';
		stringstream sopt(opt);
		sopt >> opt;
		if(opt == "t") sopt >> T;
		if(opt == "u") sopt >> u;
		if(opt == "sigma") sopt >> sigma1;
		if(opt == "scale") sopt >> scale;
	}

	n1.set_points(dens_x, dens_y);
	vector<double> n(x_size);	
	vector<double> nm(x_size);	
	vector<double> next(x_size);
	n[0] = 1;
	for(double t = tau; t <= T; t += tau)
	{
		next[0] = 1;
		nm[0]+=tau*sigma(0)*n[0];
		for(size_t i = 1; i < x_size; ++i)
		{
			next[i] = n[i]*(1 - u*tau/h - tau*sigma(i*h)) + n[i-1]*u*tau/h;
			nm[i]+=tau*sigma(i*h)*n[i];
		}
		n.swap(next);
	}

	// printing results for each region
	cout << 0 << ' ' << scale*nm[0] << endl;
	cout << 500 << ' ' << scale*nm[0.5/h] << endl;
	cout << 1160 << ' ' << scale*nm[1.160/h] << endl;
	cout << 1850 << ' ' << scale*nm[1.850/h] << endl;
	cout << 2150 << ' ' << scale*nm[2.150/h] << endl;
	cout << 3600 << ' ' << scale*nm[3.600/h] << endl;
}

