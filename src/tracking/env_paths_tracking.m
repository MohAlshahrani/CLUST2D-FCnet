function paths = env_paths_tracking(varargin)
    paths.net_base = 'D:\CSE600\Project1\cfnet-master\pretrained\'; % e.g. '/home/luca/cfnet/networks/';
    paths.eval_set_base = 'D:\CSE600\Project1\cfnet-master\data\'; % e.g. '/home/luca/cfnet/data/';
    paths.stats = 'D:\CSE600\Project1\cfnet-master\data\cfnet_ILSVRC2015.stats.mat'; % e.g.'/home/luca/cfnet/data/ILSVRC2015.stats.mat';
    paths = vl_argparse(paths, varargin);
end
