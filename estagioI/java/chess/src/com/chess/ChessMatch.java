
package com.chess;

import com.boardgame.*;
import com.chess.*;
import com.chess.pieces.*;

public class ChessMatch{
	
	private Board board;

	public ChessMatch(){
		board = new Board(8, 8);
		initialSetup();
	}


	public ChessPiece[][] getPieces(){
		ChessPiece[][] mat = new ChessPiece[board.getRows()][board.getColumns()];
		for(int i = 0; i < board.getRows(); i++){
			for(int j = 0; j < board.getColumns(); j++){
				mat[i][j] = (ChessPiece) board.piece(i, j);
			}
		}
		return mat;
	}

	private void placeNewPiece(char column, int row, ChessPiece piece){
		board.placePiece(piece, new ChessPosition(column, row).toPosition());
	}

	private void initialSetup(){
		placeNewPiece('b', 5, new Rook(board, Color.WHITE));
		placeNewPiece('a', 7, new King(board, Color.BLACK));
		placeNewPiece('c', 1, new Rook(board, Color.WHITE));
	}
}


