function AME46_outer(U, tt, chr1, chr2, j0, k0)
% -----------------------------------------------------------------------------
% 2022-03-18
%
% input:
%    chrX = chess row number X; X in [6]
%    j0, k0 = coordinates of a 6x6 sub-block of the inner structure;
%    j0 and k0 in [6]
%
% We prepare a 6x6 array out of matrix representation of AME(4,6);
% each cell in the array (6x6 chessboard) is a row from U.
% Then we prepare outer product of two rows: chr1^th row and chr2^th row
% to check if the condition of Grzegorz and Albert is fulfilled.
% Additionally, we display a particular block at position [j0, k0] to show
% its internal structure, before summing up and taking the partial trace.
%
% -----------------------------------------------------------------------------
%
% Eg. take the outer product of 1^st and 2^nd row of the 6x6 array
% (that is the outer product of the 1^st row of U with the 7^th row of U,
% up to 6^th row of U with 12^th row of U). Finally, show the details
% of the last block of the outer product:
%
%     >> AME46_outer(AME46_ORIGINAL(), 'rows', 1,2, 6,6)
%
%     >> AME46_outer(R(AME46_ORIGINAL()), 'rows', 5,6, 4,5)
%
%     >> Y = get_AME46(...);
%     >> AME46_outer(R(Tx(Y,2,[6 6])), 'cols', 3,3, 1,6)
%
% -----------------------------------------------------------------------------
%
% 2022-03-27
% j0 and k0 should be considered OBSOLETE!
% -----------------------------------------------------------------------------

    addpath ../AME46
    addpath ../matrix_tool

    for j=1:6 % each field in a66 is a row from U
    for k=1:6 % treated now as |ket>
        a66{j,k}=transpose(U((j-1)*6+k, :));
    end,end


    s = 0;
    for j=1:6
        if tt=='rows'
            s += a66{chr1, j} * a66{chr2, j}';
        end
        if tt=='cols'
            s += a66{j, chr1} * a66{j, chr2}';
        end
    end
    % mustBe36 = size(s)

    if chr1==chr2
        disp("diagonal condition:");
    else
        disp("off-diagonal condition:");
    end

    Tr_1 = round(pTrace(s, 1, [6 6])); % G&A conditions
    Tr_2 = round(pTrace(s, 2, [6 6])); % G&A conditions
    if norm(Tr_1-eye(6),'fro')<1e-13
        printf("Tr_1 = I_6\n");
    else
        printf("Tr_1 = zero matrix\n");
    end
    if norm(Tr_2-eye(6), "fro")<1e-13
        printf("Tr_2 = I_6\n");
    else
        printf("Tr_2 = zero matrix\n");
    end



    printf("structure of inner product of %s %d and %d:\n", tt, chr1, chr2);
    for j=1:36
    for k=1:36
        if abs(s(j,k))<1e-14
            s(j,k)=0;
        end
    end,end

    printcf(unitize(s));
%    nnz=sum(sum(unitize(s)))
%    printf("components of block at %d and %d:\n", j0, k0);
%    for j = 1:6;
%        tt = transpose(U((chr1-1)*6 + j,:)) * conj(U((chr2-1)*6 + j,:));
%        tt((j0-1)*6+1:(j0-1)*6+6,(k0-1)*6+1:(k0-1)*6+6)
%    end

end
