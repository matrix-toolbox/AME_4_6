function U = AME46
%
%	2020-09-02
%	2021-01-11
%
%	Suhail Ahmad Rather
%	Adam Burchardt
%	Wojciech Bruzda
%	Grzegorz Rajchel-Mieldzioc
%	Arul Lakshminarayan
%	Karol Zyczkowski
%
%	https://arxiv.org/abs/2104.05122
%
% ------------------------------------------------------------------------------
%
% it returns U such that
% svd(U) = svd(U^R) = svd(U^G) = [1 1 1 ... 1] = vector of 36 ones
% where ^R := reshuffling
%       ^G := partial transpose (w.r.t. 2nd subsystem)
%
% in other words
% it returns a complex representation of the AME(4,6) state
%
% call:
% >> U = AME46;

a = 1 / sqrt(5 + sqrt(5));
b = sqrt((5 + sqrt(5)) / 20);
c = 1 / sqrt(2);
w = exp(i * pi / 10);

U = zeros(36);

% 20 non-zero entries of 1st six rows:
        U(2, 2) = c*w^3;
        U(6, 1) = c/w;
        U(1, 8) = b/w;
        U(3, 7) = a/w^7;
        U(4, 7) = b*w^2;
        U(6, 8) = a/w^3;
        U(1, 16) = a/w^2;
        U(2, 15) = b*w^9;
        U(5, 15) = a*w^5;
        U(6, 16) = b*w^6;
        U(3, 21) = a/w^6;
        U(4, 21) = b/w;
        U(5, 22) = c/w;
        U(2, 30) = a;
        U(3, 29) = b*w^7;
        U(4, 29) = a*w^2;
        U(5, 30) = b*w^6;
        U(1, 35) = c*w^6;
        U(3, 36) = b/w^5;
        U(4, 36) = a/w^6;

% 20 non-zero entries of 2nd six rows:
        U(7, 1) = c;
        U(11, 2) = c/w^4;
        U(7, 8) = a*w^8;
        U(9, 7) = b/w^8;
        U(10, 7) = a/w^9;
        U(12, 8) = b/w^4;
        U(7, 16) = b/w^3;
        U(8, 15) = a*w^6;
        U(11, 15) = b/w^8;
        U(12, 16) = a/w^5;
        U(9, 21) = b*w;
        U(10, 21) = a/w^4;
        U(8, 22) = c*w^10;
        U(9, 29) = a/w^4;
        U(10, 29) = b*w;
        U(8, 30) = b*w^7;
        U(11, 30) = a*w^3;
        U(9, 36) = a/w^8;
        U(10, 36) = b*w;
        U(12, 35) = c/w^7;

% 18 non-zero entries of 3rd six rows:
        U(14, 6) = b/w^3;
        U(15, 5) = b/w^4;
        U(16, 5) = a/w;
        U(17, 6) = a*w^9;
        U(13, 12) = a*w^4;
        U(14, 11) = a*w^6;
        U(17, 11) = b*w^8;
        U(18, 12) = b;
        U(16, 14) = c/w^5;
        U(17, 13) = c*w;
        U(15, 19) = c;
        U(18, 20) = c/w^6;
        U(13, 27) = c*w^8;
        U(15, 28) = a*w^6;
        U(16, 28) = b/w;
        U(13, 34) = b/w^6;
        U(14, 33) = c/w^6;
        U(18, 34) = a;

% 18 non-zero entries of 4th six rows:
        U(20, 6) = a/w^3;
        U(21, 5) = a/w^8;
        U(22, 5) = b*w^5;
        U(23, 6) = b/w;
        U(19, 12) = b*w^2;
        U(20, 11) = b/w^4;
        U(23, 11) = a*w^8;
        U(24, 12) = a*w^8;
        U(20, 13) = c/w;
        U(21, 14) = c/w^2;
        U(19, 20) = c*w^6;
        U(22, 19) = c/w;
        U(24, 27) = c*w^2;
        U(21, 28) = b/w^8;
        U(22, 28) = a/w^5;
        U(19, 34) = a*w^2;
        U(23, 33) = c*w^6;
        U(24, 34) = b/w^2;

% 18 non-zero entries of 5th six rows:
        U(25, 3) = a;
        U(27, 4) = a*w;
        U(28, 4) = b*w^2;
        U(30, 3) = b;
        U(26, 10) = b*w;
        U(27, 9) = b*w^3;
        U(28, 9) = a/w^6;
        U(29, 10) = a*w;
        U(25, 17) = b/w^4;
        U(27, 18) = c/w^5;
        U(30, 17) = a*w^6;
        U(25, 24) = c/w^7;
        U(26, 23) = a/w^2;
        U(29, 23) = b*w^8;
        U(26, 26) = c/w^6;
        U(30, 25) = c;
        U(28, 32) = c/w^2;
        U(29, 31) = c/w^6;

% 18 non-zero entries of last six rows:
        U(31,3) = b/w^9;
        U(33,4) = b;
        U(34,4) = a/w^9;
        U(36,3) = a*w;
        U(32,10) = a/w^6;
        U(33,9) = a/w^8;
        U(34,9) = b/w^7;
        U(35,10) = b*w^4;
        U(31,17) = a/w^3;
        U(34,18) = c/w^5;
        U(36,17) = b/w^3;
        U(32,23) = b*w;
        U(35,23) = a*w;
        U(36,24) = c*w^4;
        U(31,25) = c*w;
        U(35,26) = c*w^7;
        U(32,31) = c/w^3;
        U(33,32) = c*w^6;


