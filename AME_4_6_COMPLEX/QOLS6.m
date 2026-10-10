function QOLS6
% ------------------------------------------------------------------------------
% 2022-03-19
%
% Recovering QOLS(6)...
% ------------------------------------------------------------------------------

    w = exp(2j*pi/20);
    a = sqrt(1 - 1/sqrt(5))/2;
    b = sqrt(1 + 1/sqrt(5))/2;
    c = 1/sqrt(2);

    % check Definition 4 from PRL
    U = AME46();
    SL3(U, "minimal");
    d = 6;
    for j=1:d
    for k=1:d
%       C{j,k}=U((j-1)*d+1:(j-1)*d+d, (k-1)*d+1:(k-1)*d+d);
        C{j, k}= reshape(U(:, (j-1)*d+k), d, d);
    end,end


    AME_CONFIRMATION = zeros(d^2);
    % reconstruct AME from blocks C{j,k} to check correctness
    for j=1:d
    for k=1:d
        AME_CONFIRMATION((j-1)*d+1:(j-1)*d+d, (k-1)*d+1:(k-1)*d+d) = C{j, k};
    end, end
    SL3(AME_CONFIRMATION, "minimal"); % must be [1 1 1]

    S1=zeros(d^2);
    for j=1:d
    for ell=1:d
        T = zeros(d);
        for i=1:d
            T += C{i,j}*C{i,ell}';
        end
        S1((j-1)*d+1:(j-1)*d+6,(ell-1)*d+1:(ell-1)*d+6) = T;
    end,end
    printcf(S1);

    printf("--------------------------------------------------------------------------\n");

    S2=zeros(d^2);
    for i=1:d
    for k=1:d
        T = zeros(d);
        for j=1:d
            T += C{i,j}*C{k,j}';
        end
        S2((i-1)*d+1:(i-1)*d+6,(k-1)*d+1:(k-1)*d+6) = T;
    end,end
    printcf(S2);

%   THIS SHOULD OBTAINED FROM THE officers.m SCRIPT!
    %fjk : f=figure, j=row, k=column
    f11 = c*ket(1) + c*ket(2);
    f12 = c*w^17*ket(1) + c*w^19*ket(2);
    f13 = a*w^18*ket(5) + b*w^3*ket(5) + b*w^3*ket(6) + a*w^18*ket(6);
    f14 = a*w^3*ket(5) + b*ket(5) + b*ket(6) + a*w^7*ket(6);
    f15 = b*ket(3) + a*w^5*ket(3) + a*w^5*ket(4) + b*ket(4);
    f16 = b*w^14*ket(3) + a*w*ket(3) + a*w^15*ket(4) + b*w^12*ket(4);
    Bf1_= [f11 f12 f13 f14 f15 f16]; % basis # 1
    detBf1 = det(Bf1_);

    f21 = c*ket(5) + c*ket(6);
    f22 = c*w^7*ket(5) + c*w^19*ket(6);
    f23 = a*w^2*ket(3) + b*w^19*ket(3) + b*w^13*ket(4) + a*ket(4);
    f24 = c*w^10*ket(3) + c*w^6*ket(4);
    f25 = a*w^2*ket(1) + b*w*ket(1) + b*w^5*ket(2) + a*w^14*ket(2);
    f26 = b*w^4*ket(1) + a*w^3*ket(1) + a*w^9*ket(2) + b*w^18*ket(2);
    Bf2_= [f21 f22 f23 f24 f25 f26]; % basis # 2
    detBf2 = det(Bf2_);

    f31 = c*w^8*ket(3) + c*w^16*ket(4);
    f32 = c*w^2*ket(3) + c*w^2*ket(4);
    f33 = c*w^5*ket(1) + c*w^19*ket(2);
    f34 = a*w^1*ket(1) + b*w^10*ket(1) + b*w^4*ket(2) + a*w^3*ket(2);
    f35 = c*w^13*ket(5) + c*w^7*ket(6);
    f36 = a*w^12*ket(5) + b*w^15*ket(5) + b*w*ket(6) + a*w^14*ket(6);
    Bf3_= [f31 f32 f33 f34 f35 f36]; % basis # 3
    detBf3 = det(Bf3_);

    f41 = a*w^1*ket(1) + b*w^14*ket(1) + b*w^16*ket(2) + a*w^19*ket(2);
    f42 = b*w^10*ket(1) + a*w^5*ket(1) + a*w^15*ket(2) + b*ket(2);
    f43 = b*w^14*ket(5) + a*w^7*ket(5) + a*w^13*ket(6) + b*w^16*ket(6);
    f44 = b*w^10*ket(5) + a*w^5*ket(5) + a*w^5*ket(6) + b*w^10*ket(6);
    f45 = a*w^4*ket(3) + b*w^17*ket(3) + b*w^7*ket(4) + a*w^10*ket(4);
    f46 = a*ket(3) + b*w^15*ket(3) + b*w^15*ket(4) + a*ket(4);
    Bf4_= [f41 f42 f43 f44 f45 f46]; % basis # 4
    detBf4 = det(Bf4_);

    f51 = c*w^14*ket(5) + c*w^10*ket(6);
    f52 = c*ket(5) + c*w^10*ket(6);
    f53 = b*w^7*ket(3) + a*w^10*ket(3) + a*ket(4) + b*w^13*ket(4);
    f54 = c*ket(3) + c*w^10*ket(4);
    f55 = b*w^2*ket(1) + a*w^5*ket(1) + a*w^15*ket(2) + b*w^8*ket(2);
    f56 = c*ket(1) + c*ket(2);
    Bf5_= [f51 f52 f53 f54 f55 f56]; % basis # 5
    detBf5 = det(Bf5_);

    f61 = c*ket(3) + c*w^10*ket(4);
    f62 = c*w^6*ket(3) + c*ket(4);
    f63 = a*w^10*ket(1) + b*w^15*ket(1) + b*w^5*ket(2) + a*ket(2);
    f64 = b*w^14*ket(1) + a*w^3*ket(1) + a*w^7*ket(2) + b*w^6*ket(2);
    f65 = c*w*ket(5) + c*w^11*ket(6);
    f66 = b*w^9*ket(5) + a*w^16*ket(5) + a*w^16*ket(6) + b*w^13*ket(6);
    Bf6_=[f61 f62 f63 f64 f65 f66 ]; % basis # 6
    detBf6 = det(Bf6_);

    % cjk : c=color, j=row, k=column
    c11 = c*ket(2) + c*ket(1);
    c12 = c*w^17*ket(3) + c*w^19*ket(4);
    c13 = a*w^18*ket(5) + b*w^3*ket(6) + b*w^3*ket(5) + a*w^18*ket(6);
    c14 = a*w^3*ket(1) + b*ket(2) + b*ket(1) + a*w^7*ket(2);
    c15 = b*ket(3) + a*w^5*ket(4) + a*w^5*ket(3) + b*ket(4);
    c16 = b*w^14*ket(5) + a*w*ket(6) + a*w^15*ket(5) + b*w^12*ket(6);
    Bc1_= [c11 c12 c13 c14 c15 c16]; % basis # c1
    detBc1 = det(Bc1_);
    c21 = c*ket(2) + c*ket(1);
    c22 = c*w^7*ket(3) + c*w^19*ket(4);
    c23 = a*w^2*ket(5) + b*w^19*ket(6) + b*w^13*ket(5) + a*ket(6);
    c24 = c*w^10*ket(1) + c*w^6*ket(2);
    c25 = a*w^2*ket(3) + b*w*ket(4) + b*w^5*ket(3) + a*w^14*ket(4);
    c26 = b*w^4*ket(5) + a*w^3*ket(6) + a*w^9*ket(5) + b*w^18*ket(6);
    Bc2_= [c21 c22 c23 c24 c25 c26]; % basis # c2
    detBc2 = det(Bc2_);
    c31 = c*w^8*ket(5) + c*w^16*ket(6);
    c32 = c*w^2*ket(2) + c*w^2*ket(1);
    c33 = c*w^5*ket(4) + c*w^19*ket(3);
    c34 = a*w^1*ket(5) + b*w^10*ket(6) + b*w^4*ket(5) + a*w^3*ket(6);
    c35 = c*w^13*ket(1) + c*w^7*ket(2);
    c36 = a*w^12*ket(3) + b*w^15*ket(4) + b*w*ket(3) + a*w^14*ket(4);
    Bc3_= [c31 c32 c33 c34 c35 c36]; % basis # c3
    detBc3 = det(Bc3_);
    c41 = a*w^1*ket(5) + b*w^14*ket(6) + b*w^16*ket(5) + a*w^19*ket(6);
    c42 = b*w^10*ket(1) + a*w^5*ket(2) + a*w^15*ket(1) + b*ket(2);
    c43 = b*w^14*ket(3) + a*w^7*ket(4) + a*w^13*ket(3) + b*w^16*ket(4);
    c44 = b*w^10*ket(5) + a*w^5*ket(6) + a*w^5*ket(5) + b*w^10*ket(6);
    c45 = a*w^4*ket(1) + b*w^17*ket(2) + b*w^7*ket(1) + a*w^10*ket(2);
    c46 = a*ket(3) + b*w^15*ket(4) + b*w^15*ket(3) + a*ket(4);
    Bc4_= [c41 c42 c43 c44 c45 c46]; % basis # c4
    detBc4 = det(Bc4_);
    c51 = c*w^14*ket(4) + c*w^10*ket(3);
    c52 = c*ket(6) + c*w^10*ket(5);
    c53 = b*w^7*ket(1) + a*w^10*ket(2) + a*ket(1) + b*w^13*ket(2);
    c54 = c*ket(3) + c*w^10*ket(4);
    c55 = b*w^2*ket(5) + a*w^5*ket(6) + a*w^15*ket(5) + b*w^8*ket(6);
    c56 = c*ket(1) + c*ket(2);
    Bc5_= [c51 c52 c53 c54 c55 c56]; % basis # c5
    detBc5 = det(Bc5_);
    c61 = c*ket(4) + c*w^10*ket(3);
    c62 = c*w^6*ket(6) + c*ket(5);
    c63 = a*w^10*ket(1) + b*w^15*ket(2) + b*w^5*ket(1) + a*ket(2);
    c64 = b*w^14*ket(3) + a*w^3*ket(4) + a*w^7*ket(3) + b*w^6*ket(4);
    c65 = c*w*ket(5) + c*w^11*ket(6);
    c66 = b*w^9*ket(1) + a*w^16*ket(2) + a*w^16*ket(1) + b*w^13*ket(2);
    Bc6_= [c61 c62 c63 c64 c65 c66]; % basis # c6
    detBc6 = det(Bc6_);

    Tracef11c51 = trace(f11.*c51)
    Tracef12c52 = trace(f12.*c52)
    Tracef13c53 = trace(f13.*c53)
    Tracef14c54 = trace(f14.*c54)
    Tracef15c55 = trace(f15.*c55)
    Tracef16c56 = trace(f16.*c56)

    % Bf1_.*Bc1_'
end

function v=ket(j)
    v = zeros(6, 1);
    v(j) = 1;
end
