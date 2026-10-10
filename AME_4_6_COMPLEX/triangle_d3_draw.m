function triangle_d3_draw
% ------------------------------------------------------------------------------
% 2021-08-28
%
% Draw ep-gt plane for d = 3 with all possible permutation matrices of size 9.
% ------------------------------------------------------------------------------

    hold all
    draw_edges(0);
    load triangle_d3.dat;

    for j=1:size(ppc,1)
        scatter(ppc(j,:)(1), ppc(j,:)(2), 10, "k", "filled");
    end

end

