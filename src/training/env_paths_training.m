function opts = env_paths_training(opts)
    opts.rootDataDir = '/Users/mohammed/MATLAB/Projects/cfnet-master/new_dataset/data/anything/'; % where the training set is
    opts.imdbVideoPath = '/Users/mohammed/MATLAB/Projects/cfnet-master/ILSVRC15-curation/imdb_video.mat'; % where the training set metadata are
    opts.imageStatsPath = '/Users/mohammed/MATLAB/Projects/cfnet-master/ILSVRC15-curation/anything_stats.mat'; % where the training set stats are
end
