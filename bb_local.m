function bb_local
%------------------------------------------------------------------------------
% 2022-04-01
%
% 1st bell basis of U from 9x4=6x6 paper: J. Phys.: Conf. Ser. 2448, 012003 (2023).
% presented as:
%
% (U_1 (x) U_2) * Bell_BASIS * diag(PHASES)
%------------------------------------------------------------------------------

        b1 = getBlock1()

%       constants calculated "manually" in Mathematica by GRM
        theta = pi/4;
        thetaPrime = pi/4;
        phi1 = - atan(2)/4 - 3*pi/20;
        phi2 = - phi1 + 6*pi/5;
        phi1Prime = -phi1 - pi/10;
        phi2Prime = -phi2 - pi/10;
        globalPhase = diag(exp(1j*pi*[3/10, -1/5, 1/5, 1]));
%       constants calculated "manually" in Mathematica

        u2xu2 = kron(u2(phi1, phi2, theta), u2(phi1Prime, phi2Prime, thetaPrime))

        BellBasis = [    % one of many possible representations
            0  1  1  0;  %  = |01> + |10>
            1  0  0  1;  %  = |00> + |11>
            1  0  0 -1;  %  = |00> - |11>
            0  1 -1  0;  %  = |01> - |10>
        ]/sqrt(2);

        b1_decomposition = transpose(u2xu2*transpose(BellBasis)*globalPhase)

        confirmation = (b1_decomposition - b1 < eps*2) % should be all-ones matrix

end



function u = u2(phi1, phi2, theta)
% general unitary matrix of size 2x2
% here without "global" phase, which has been absorbed into globalPhase above
    u = [
         exp(+1j*phi1)*cos(theta)    exp(+1j*phi2)*sin(theta);
        -exp(-1j*phi2)*sin(theta)    exp(-1j*phi1)*cos(theta);
    ];
end



function block4x4 = getBlock1
% first 4x4 block from U brought to the 9x(4x4) block diagonal form
% with two permutations P1 and P2 presented in 9x4=6x6 paper
    a = sqrt(1 - 1/sqrt(5))/2;
    b = sqrt(1 + 1/sqrt(5))/2;
    c = 1/sqrt(2);

    amplitudes=[
        a b b a;
        c 0 0 c;
        0 c c 0;
        b a a b;
    ];
    phases = [
         2  1  5 -6;
        -3  0  0 -1
         0  5 -1  0;
        -6  3  7  6;
    ];
    block4x4 = e.^(1j*pi*phases/10) .* amplitudes;

end


% example of output
%
% b1 =
%
%    3.0075e-01 + 2.1851e-01i   5.7206e-01 + 1.8587e-01i   3.6831e-17 + 6.0150e-01i  -1.1488e-01 - 3.5355e-01i
%    4.1563e-01 - 5.7206e-01i            0 +          0i            0 +          0i   6.7250e-01 - 2.1851e-01i
%             0 +          0i   4.3298e-17 + 7.0711e-01i   6.7250e-01 - 2.1851e-01i            0 +          0i
%   -1.8587e-01 - 5.7206e-01i   2.1851e-01 + 3.0075e-01i  -2.1851e-01 + 3.0075e-01i  -1.8587e-01 + 5.7206e-01i
%
% u2xu2 =
%
%    4.7553e-01 - 1.5451e-01i   3.8143e-01 + 3.2328e-01i   1.1857e-01 - 4.8574e-01i   4.7553e-01 - 1.5451e-01i
%    2.9389e-01 + 4.0451e-01i   1.8959e-01 - 4.6266e-01i   4.9860e-01 - 3.7337e-02i  -2.9389e-01 - 4.0451e-01i
%    2.9389e-01 - 4.0451e-01i   4.9860e-01 + 3.7337e-02i   1.8959e-01 + 4.6266e-01i  -2.9389e-01 + 4.0451e-01i
%    4.7553e-01 + 1.5451e-01i  -1.1857e-01 - 4.8574e-01i  -3.8143e-01 + 3.2328e-01i   4.7553e-01 + 1.5451e-01i

% b1_decomposition =
%
%    3.0075e-01 + 2.1851e-01i   5.7206e-01 + 1.8587e-01i  -2.7756e-16 + 6.0150e-01i  -1.1488e-01 - 3.5355e-01i
%    4.1563e-01 - 5.7206e-01i  -1.0174e-17 - 6.1224e-17i  -5.5083e-17 - 2.8595e-17i   6.7250e-01 - 2.1851e-01i
%    6.9381e-17 - 1.0535e-18i   3.3307e-16 + 7.0711e-01i   6.7250e-01 - 2.1851e-01i  -2.0438e-17 - 6.6311e-17i
%   -1.8587e-01 - 5.7206e-01i   2.1851e-01 + 3.0075e-01i  -2.1851e-01 + 3.0075e-01i  -1.8587e-01 + 5.7206e-01i
%
% confirmation =
%
%   1  1  1  1
%   1  1  1  1
%   1  1  1  1
%   1  1  1  1



