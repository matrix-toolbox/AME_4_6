function U = AME46_ORIGINAL
% ------------------------------------------------------------------------------
%
%       2020-09-02 first release of AME(4, 6) in analytical form
%       2023-03-07 last update
%
%       Suhail Ahmad Rather
%       Adam Burchardt
%       Wojciech Bruzda
%       Grzegorz Rajchel-Mieldzioc
%       Arul Lakshminarayan
%       Karol Zyczkowski
%
%       Phys. Rev. Lett. 128, 080507 (2022)
%       https://doi.org/10.1103/PhysRevLett.128.080507
%       https://arxiv.org/abs/2104.05122
%
%       see also:
%       J. Phys.: Conf. Ser. 2448, 012003 (2023)
%       https://doi.org/10.1088/1742-6596/2448/1/012003
%
% ------------------------------------------------------------------------------
%
% Function AME46 returns a unitary matrix U of order 36 such that
% svd(U) = svd(U^R) = svd(U^G) = [1 1 1 ... 1] = vector of 36 ones
% where ^R := reshuffling
%       ^G := partial transpose (w.r.t. 2^nd subsystem)
%
% In other words,
% it returns a complex representation of the AME(4, 6) state.
%
% ------------------------------------------------------------------------------
%
% Call:
% >> U = AME46_ORIGINAL;
%
% ------------------------------------------------------------------------------
    a = sqrt(1 - 1 / sqrt(5)) / 2;
    b = sqrt(1 + 1 / sqrt(5)) / 2;
    c = 1 / sqrt(2);
    w = exp(2j * pi / 20);

    U = [
        0 c 0 0 0 0,c 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 c 0 0 0,0 0 0 c 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 a b,0 0 0 0 b a;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,a b 0 0 0 0,b a 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 b a 0 0,0 0 a b 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 b a,0 0 0 0 a b,0 0 0 0 0 0,0 0 0 0 0 0;

        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 c 0 0 0 0,c 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 c 0 0 0,0 0 0 c 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 a b,0 0 0 0 b a,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,c 0 0 0 0 0,0 c 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 a b 0 0,0 0 b a 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 b a,0 0 0 0 a b,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;

        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 c 0,0 0 0 0 0 c,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 c 0 0 0 0,c 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 c 0 0,0 0 c 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 a b,0 0 0 0 b a,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,c 0 0 0 0 0,0 c 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 a b 0 0,0 0 b a 0 0;

        0 0 0 0 a b,0 0 0 0 b a,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        b a 0 0 0 0,a b 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 b a 0 0,0 0 a b 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 b a,0 0 0 0 a b;
        0 0 0 0 0 0,0 0 0 0 0 0,a b 0 0 0 0,b a 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 a b 0 0,0 0 b a 0 0,0 0 0 0 0 0,0 0 0 0 0 0;

        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 c 0 0,0 0 c 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 c,0 0 0 0 c 0;
        0 0 0 0 0 0,0 0 0 0 0 0,b a 0 0 0 0,a b 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 c 0 0 0,0 0 0 c 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 b a,0 0 0 0 a b,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        c 0 0 0 0 0,0 c 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;

        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 c 0 0,0 0 c 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 c,0 0 0 0 c 0,0 0 0 0 0 0,0 0 0 0 0 0;
        a b 0 0 0 0,b a 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 b a 0 0,0 0 a b 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 c 0,0 0 0 0 0 c;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,b a 0 0 0 0,a b 0 0 0 0;
    ] .* w.^[
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0 17  0  0  0, 0  0  0 19  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0 18  3, 0  0  0  0  3 18;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 3  0  0  0  0  0, 0  7  0  0  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  5  0  0, 0  0  5  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0 14  1, 0  0  0  0 15 12, 0  0  0  0  0  0, 0  0  0  0  0  0;

         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0,10  0  0  0  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  7  0  0  0, 0  0  0 19  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  2 19, 0  0  0  0 13  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0,10  0  0  0  0  0, 0  6  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  2  1  0  0, 0  0  5 14  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  0  0  4  3, 0  0  0  0  9 18, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;

         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  8  0, 0  0  0  0  0 16, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  2  0  0  0  0, 2  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  0  5  0  0, 0  0 19  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  0  0  1 10, 0  0  0  0  4  3, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0,13  0  0  0  0  0, 0  7  0  0  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0 12 15  0  0, 0  0  1 14  0  0;

         0  0  0  0  1 14, 0  0  0  0 16 19, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
        10  5  0  0  0  0,15  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0 14  7  0  0, 0  0 13 16  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0 10  5, 0  0  0  0  5 10;
         0  0  0  0  0  0, 0  0  0  0  0  0, 4 17  0  0  0  0, 7 10  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0 15  0  0, 0  0 15  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;

         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0 14  0  0, 0  0 10  0  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0 10  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 7 10  0  0  0  0, 0 13  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0 10  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  0  0  2  5, 0  0  0  0 15  8, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;

         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0 10  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0 16, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
        10 15  0  0  0  0, 5  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0 14  3  0  0, 0  0  7  6  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  1  0, 0  0  0  0  0 11;
         0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 0  0  0  0  0  0, 9 16  0  0  0  0,16 13  0  0  0  0;
    ];

end
