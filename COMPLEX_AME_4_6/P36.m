function U = P36(m)
% 2018-01-15
% AOLS = Almost Orthogonal Latin Squares
% C = P36(3) => e_p(C) = 0.712018140589569
%
% USE m=3 to get Unitary representation!
%
% references included in the code below

%  m = 3;
  d = 6;

  try
    OLS = getOLS(m);
  catch
    printf("=======================================================================\n");
    printf("ERROR! missing 'm'! 1=Horton, 2=Clarisse(\\hat{P}), 3=Clarisse(\tilde{P})\n");
    printf("=======================================================================\n");
    U=[];
    return
  end
  O1 = OLS{1};
  O2 = OLS{2};
  for j = 1 : d
    for k = 1 : d
      C(j, k) = str2num(strcat(int2str(O1(j, k)), int2str(O2(j, k))));
    end
  end
  M = zeros(d, d);
  j = 1 : d;
  k = 1 : d;
    M(j, k) = mod(C(j, k), 10) + d * fix(C(j, k) / 10);
  M = reshape(transpose(M), 1, d^2);
  I = eye(d^2); % prepare ~permutation matrix
  U = [];
  k = 1 : d^2;
    U = [U; I(M(k) + 1, :)];
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function OLS = getOLS(m)
  switch m
  case 1
    % cf. J.D. Horton (1972) http://www.sciencedirect.com/science/article/pii/0097316574900697  
    OLS{1} = [
      5 6 3 4 1 2;
      2 1 6 5 3 4;
      6 5 1 2 4 3;
      4 3 5 6 2 1;
      1 4 2 3 5 6;
      3 2 4 1 6 5;
    ] - 1;
    OLS{2} = [
      1 2 5 6 3 4;
      6 5 1 2 4 3;
      4 3 6 5 1 2;
      5 6 4 3 2 1;
      2 4 3 1 6 5;
      3 1 2 4 6 5;
    ] - 1;
    % C = [ % for a future test...
    %    0 11 22 33 44 55;
    %   12  3 34 25 50 41;
    %   21 30 53 42  5 14;
    %   35 24 40 51 13  2;
    %   43 52 15  4 31 20;
    %   54 45  1 10 22 33;
    % ]
  case 2
    % Clarisse et al. "Entangling Power of Permutations"
    % quant-ph/0502040v2 (5) \tilde{P} (NOT UNITARY! -- NEEDS RESHUFFLING!)
    OLS{1} = [
      1 2 3 4 5 6;
      2 1 4 3 6 5;
      3 4 6 5 1 2;
      4 3 5 6 2 1;
      5 6 2 1 4 3;
      6 5 1 2 3 4;
    ] - 1;
    OLS{2} = [
      1 2 3 4 5 6;
      3 4 5 6 1 2;
      2 1 4 3 6 5;
      6 5 1 2 4 3;
      4 3 6 5 2 1;
      5 6 2 1 3 4;
    ] - 1;
  case 3
    % Clarisse et al. "Entangling Power of Permutations"
    % quant-ph/0502040v2
    % -- alternative formula: \hat{P} (UNITARY)
    %
    % THIS IS THE STARTING POINT FOR OUR RESEARCH
    %
    OLS{1} = [
      1 2 3 4 5 6;
      2 1 4 3 6 5;
      5 6 1 2 4 3;
      6 5 2 1 3 4;
      4 3 6 5 1 2;
      3 4 5 6 2 1;
    ] - 1;
    OLS{2} = [
      1 2 3 4 5 6;
      4 3 6 5 2 1;
      6 5 2 1 3 4;
      3 4 5 6 1 2;
      5 6 1 2 4 3;
      2 1 3 4 6 5;
    ] - 1;
  otherwise
    error('Not implemented!')
  end

end

