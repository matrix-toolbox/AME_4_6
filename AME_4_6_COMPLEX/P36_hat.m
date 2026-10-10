function P = P36_hat
% ------------------------------------------------------------------------------
% 2021-07-27
%
% Permutation matrix hat_P (Clarisse et al.) constructed using basis vectors.
% ------------------------------------------------------------------------------

    hP = [
        11  22  33  44  55  66;
        23  14  45  36  61  52;
        32  41  64  53  16  25;
        46  35  51  62  24  13;
        54  63  26  15  42  31;
        65  56  12  21  33  44;
    ];


    P = zeros(36);

    for r=1:6 % go from left to right, top to bottom
%        disp(sprintf('--------------------'));
    for c=1:6
        j = floor(hP(r,c) / 10);
        k = mod(hP(r,c), 10);
%        disp(sprintf('%d ---> %d %d', hP(r,c), j, k));

        P += kron(ket(r), ket(c)) * transpose(kron(ket(j), ket(k)));
    end
    end

%    P
%    printcf(P)
end



function ek = ket(k) % return standard basis vector with unity at k^th position
    ek = zeros(6, 1);
    ek(k) = 1;
end
