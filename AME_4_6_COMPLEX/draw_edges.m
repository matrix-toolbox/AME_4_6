function draw_edges(x0)
% ------------------------------------------------------------------------------
% 2020-09-17
%
% Draw upper and lower edge of the ep-gt triangle.
% ------------------------------------------------------------------------------

    scale = 1; %  5/7;
    axis("square")
    %xlabel("e_p")
    %ylabel("g_t")
    %plot([x0, scale], [scale*x0, 1], ':k','linewidth',1);
    plot([x0, scale], [scale*x0, 1], "linewidth",1, "linestyle",":", "color","b");
    plot([x0, scale], [2-scale*x0, 1], "linewidth",1, "linestyle",":", "color","b");

end


