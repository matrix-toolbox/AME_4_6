function triangle_d3
% ------------------------------------------------------------------------------
% 2021-08-28
%
% Calculate the positions (on ep-gt plane) of all permutation matrices
% of order d = 3. See "triangle_d3.png".
% ------------------------------------------------------------------------------

    pp = perms(1:9);
    ppc=[];
    for j=1:size(pp, 1)
	Y = eye(9);
	Y = Y(pp(j, :), :);
	x = ep3(Y);
	y = gt3(Y);
	ppc = [ppc; x y];
    end

    clear pp;
    clear Y;
    clear x;
    clear y;

    ppc = unique(ppc, "rows")
    save("triangle_d3.dat", "*");

end

function r = ep3(U)
	d = 3; % local dimension
	S = swap(3);
	r = SL3(R(U)) + SL3(R(U * S)) - SL3(S);
%	r = r * (d^2 + 1) / d^2;
end

function r = gt3(U)
	d = 3; % local dimension
	S = swap(3);
	r = SL3(R(U)) - SL3(R(U * S)) + SL3(S);
%	r = r * (d^2 + 1) / d^2;
end

function S = SL3(U)
	d = 3; % local dimension
	f = U*U'/trace(U*U');
	S = 1 - trace(f*f);
	S = S * (d^2) / (d^2 - 1);
end

