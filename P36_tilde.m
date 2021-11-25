function P=P36_tilde
% 2021-07-27
% recover hat_P (Clarisse et al.) using basis vectors
% this is a bit simplified version of the P36.m script!

    hP = [
        11  22  33  44  55  66;
        24  13  46  35  62  51;
        56  65  12  21  43  34;
        63  54  25  16  31  42;
        45  36  61  52  14  23;
        32  41  53  64  26  15;
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



% return standard basis vector with unity at k^th position
function ek = ket(k)
    ek=zeros(6,1);
    ek(k) = 1;
end